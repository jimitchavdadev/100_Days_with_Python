import time  # Import time module for time-related operations
import requests  # Import requests module for making HTTP requests
from datetime import datetime  # Import datetime module for date and time handling
import smtplib  # Import smtplib module for sending emails

# Your email address and password (replace with your actual email and password)
MY_EMAIL = "your_email@gmail.com"
MY_PASSWORD = "your_email_password"

# Your latitude and longitude (replace with your actual coordinates)
MY_LAT = 51.507351
MY_LONG = -0.127758

# Function to check if the ISS is overhead
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Check if ISS position is within +5 or -5 degrees of your position
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG:
        return True

# Function to check if it's night at your location
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    # Check if the current time is after sunset or before sunrise
    if time_now >= sunset or time_now <= sunrise:
        return True

# Run the code every 60 seconds to check ISS position and night time
while True:
    time.sleep(60)  # Wait for 60 seconds
    if is_iss_overhead() and is_night():  # If ISS is overhead and it's night time
        connection = smtplib.SMTP("smtp.gmail.com")  # Connect to Gmail SMTP server
        connection.starttls()  # Secure the connection
        connection.login(MY_EMAIL, MY_PASSWORD)  # Login to your email account
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: Look Up!\n\nThe ISS is above you in the sky."  # Email subject and body
        )

# This code continuously checks if the ISS is close to your position and if it's night time.
# If both conditions are true, it sends an email notification every 60 seconds.