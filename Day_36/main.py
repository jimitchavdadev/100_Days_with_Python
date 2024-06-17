import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client

# Load environment variables from .env file
load_dotenv()

# Twilio credentials loaded from environment variables
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
whatsapp_from_number = os.getenv("TWILIO_WHATSAPP_FROM_NUMBER")  # Load the Twilio WhatsApp number
whatsapp_to_number = os.getenv("YOUR_WHATSAPP_NUMBER")  # Load your WhatsApp number

# Debug prints to verify loading of environment variables
print("Twilio Account SID:", account_sid)
print("Twilio Auth Token:", auth_token)
print("WhatsApp From Number:", whatsapp_from_number)
print("WhatsApp To Number:", whatsapp_to_number)
print("Weather API Key:", os.getenv("WEATHER_API_KEY"))


# Function to send a WhatsApp message via Twilio
def send_whatsapp_message(message):
    client = Client(account_sid, auth_token)  # Initialize Twilio Client

    # Send message
    message = client.messages.create(
        body=message,
        from_=f"whatsapp: {whatsapp_from_number}",
        to=f"whatsapp: {whatsapp_to_number}"
    )

    print("Message sent successfully:", message.sid)


# Get weather API key from environment variable
api_key = os.getenv("WEATHER_API_KEY")

# Parameters for the weather API request
parameters = {
    "q": "Ahmedabad",
    "appid": api_key,
}

# Request weather data
response = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=parameters)
response.raise_for_status()
weather_data = response.json()

# Check the weather condition
weather_id = weather_data['weather'][0]['id']
will_rain = weather_id < 700

# Send appropriate message based on weather condition
if will_rain:
    message = "🌧 It's going to rain today, bring an umbrella with you."
    send_whatsapp_message(message)
else:
    message = "☀️ No rain expected today. Have a great day!"
    send_whatsapp_message(message)
