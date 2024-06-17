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


def send_whatsapp_message(message):
    """
    Sends a WhatsApp message using Twilio API.
    """
    client = Client(account_sid, auth_token)  # Initialize Twilio Client

    # Send message
    message = client.messages.create(
        body=message,
        from_=f"whatsapp:{whatsapp_from_number.strip()}",
        to=f"whatsapp:{whatsapp_to_number.strip()}"
    )

    print("Message sent successfully:", message.sid)


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

NEWS_API = "683c45554e284f72b468e7b420e3736c"  # Your News API key
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"  # Endpoint for fetching news


def stock_check():
    """
    Checks if the stock price of Tesla Inc (TSLA) has increased or decreased by 5% between yesterday and the day before yesterday.
    """
    stock_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": "TSLA",
        "apikey": "HVGF3X1SA82RWQNN"  # Your Alpha Vantage API key
    }
    stock_url = "https://www.alphavantage.co/query"  # URL for stock data
    stock_response = requests.get(url=stock_url, params=stock_parameters)  # Get stock data
    stock_response.raise_for_status()  # Raise an error for bad response
    stock_data = stock_response.json()  # Parse JSON data
    time_series_daily = stock_data["Time Series (Daily)"]  # Get daily time series data
    yesterday = list(time_series_daily.keys())[0]  # Get yesterday's date
    day_before_yesterday = list(time_series_daily.keys())[1]  # Get the day before yesterday's date
    data1 = float(time_series_daily[yesterday]["1. open"])  # Get yesterday's opening price
    data2 = float(time_series_daily[day_before_yesterday]["1. open"])  # Get the day before yesterday's opening price
    percent = (data2 - data1) * 100 / data2  # Calculate the percentage change
    if abs(percent) >= 5:  # Check if the change is at least 5%
        return True
    return False


news_parameters = {
    "apiKey": NEWS_API,
    "q": COMPANY_NAME  # Query for news about the company
}


def get_news():
    """
    Fetches the top 3 news articles for Tesla Inc from the News API.
    """
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)  # Get news data
    news_response.raise_for_status()  # Raise an error for bad response
    news_data = news_response.json()  # Parse JSON data

    news_articles = news_data["articles"][:3]  # Get the first 3 news pieces
    news_messages = []

    for article in news_articles:  # Iterate over the articles
        news_title = article["title"]  # Get the title of the article
        news_brief = article["description"]  # Get the brief description of the article
        news_message = f"Headline: {news_title}\nBrief: {news_brief}"  # Format the message
        news_messages.append(news_message)  # Append the message to the list

    return news_messages  # Return the list of news messages


if stock_check():
    # If stock price change is significant, get the news and send via WhatsApp
    news_messages = get_news()
    for news_message in news_messages:
        send_whatsapp_message(news_message)
else:
    # If stock price change is not significant, send a message indicating no significant change
    send_whatsapp_message("Stock price change is less than 5%. No news today.")

# Test message
# send_whatsapp_message("hello this is a test message")
