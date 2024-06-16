import requests  # Import the requests module for making HTTP requests
from datetime import datetime  # Import datetime module for date and time handling

# Your latitude and longitude (replace with your actual coordinates)
MY_LAT = 1234
MY_LONG = 5678

# Parameters for the API request including latitude, longitude, and format
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,  # Use 0 for unformatted date/time
}

# Send a GET request to the Sunrise-Sunset API with the specified parameters
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)

# Raise an exception if the response status code is not 200 (OK)
response.raise_for_status()

# Convert the response content to JSON format
data = response.json()

# Extract sunrise and sunset times from the JSON data
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

# Print the sunrise time
print(sunrise)

# Get the current time
time_now = datetime.now()

# Extract the hour part from the sunrise time (e.g., "2024-06-16T04:53:34+00:00" -> "04")
t = sunrise.split("T")[1].split(":")[0]

# Print the extracted hour part of the sunrise time
print(t)

# Print the current date and time
print(time_now)