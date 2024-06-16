import smtplib  # Import the smtplib module to handle email sending
from datetime import datetime  # Import datetime module to get the current date and time
import pandas  # Import pandas for data manipulation
import random  # Import random for generating random numbers

my_email = ""  # Your email address
passw = ""  # Your email password

today = datetime.now()  # Get the current date and time
today_tuple = (today.month, today.day)  # Create a tuple with the current month and day

# Read birthday data from a CSV file into a pandas DataFrame
data = pandas.read_csv("birthdays.csv")

# Create a dictionary where keys are tuples (month, day) and values are rows from the DataFrame
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# Check if today's date matches any birthday in the dictionary
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]  # Get the birthday person's information
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"  # Choose a random letter template
    with open(file_path) as letter_file:
        contents = letter_file.read()  # Read the contents of the letter template
        contents = contents.replace("[NAME]", birthday_person["name"])  # Replace placeholder with the name

    # Connect to Gmail SMTP server and send the birthday email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Secure the connection
        connection.login(my_email, passw)  # Log in to your email account
        connection.sendmail(
            from_addr=my_email,  # Your email address
            to_addrs=birthday_person["email"],  # Recipient's email address
            msg=f"Subject: Happy Birthday!\n\n{contents}"  # Subject and body of the email
        )