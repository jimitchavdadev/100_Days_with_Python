import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# Function to send a message via Telegram bot
def telegram_bot_send_text(bot_message):
    bot_token = os.getenv("BOT_TOKEN")  # Load bot token from environment variable
    bot_chatID = os.getenv("BOT_CHATID")  # Load chat ID from environment variable
    send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&parse_mode=Markdown&text={bot_message}'

    bot_response = requests.get(send_text)
    return bot_response.json()


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
    telegram_bot_send_text(message)
else:
    message = "☀️ No rain expected today. Have a great day!"
    telegram_bot_send_text(message)


# Function to get updates from the Telegram bot
def get_updates():
    bot_token = os.getenv("BOT_TOKEN")  # Load bot token from environment variable
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    response = requests.get(url)
    return response.json()


# Get and print bot updates
updates = get_updates()
print(updates)
