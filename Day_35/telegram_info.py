import requests

# Replace with your bot token
bot_token = ""


def get_updates():
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    response = requests.get(url)
    return response.json()


updates = get_updates()
print(updates)
