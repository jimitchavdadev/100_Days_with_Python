import random  # Import the random module to randomly choose a quote
import smtplib  # Import the smtplib module to handle email sending
import datetime as dt  # Import the datetime module to get the current date and time

# Function to read quotes from a file
def read_quotes(file_path):
    with open(file_path, 'r') as file:  # Open the file in read mode
        # Read the entire file content
        file_contents = file.read()

        # Split the content by newline to get individual quotes
        quotes = file_contents.split('\n')

        # Remove any empty strings that might occur due to trailing newlines
        quotes = [quote for quote in quotes if quote.strip()]

    return quotes  # Return the list of quotes

# Path to the file containing quotes
file_path = 'Birthday+Wisher+(Day+32)+start/Birthday Wisher (Day 32) start/quotes.txt'
quotes_list = read_quotes(file_path)  # Read quotes from the file
quote = random.choice(quotes_list)  # Randomly select a quote from the list

my_email = ""  # Your email address
my_email_password = ""  # Your email password

now = dt.datetime.now()  # Get the current date and time
weekday = now.weekday()  # Get the current day of the week (0=Monday, 1=Tuesday, ..., 6=Sunday)

if weekday == 5:  # Check if today is Saturday (5=Saturday)
    with smtplib.SMTP("smtp.gmail.com") as connection:  # Connect to the Gmail SMTP server
        connection.starttls()  # Secure the connection
        connection.login(user=my_email, password=my_email_password)  # Log in to your email account
        connection.sendmail(
            from_addr=my_email,  # Your email address
            to_addrs="",  # Recipient's email address
            msg=f"Subject: Testing\n\n{quote}"  # Subject and body of the email
        )