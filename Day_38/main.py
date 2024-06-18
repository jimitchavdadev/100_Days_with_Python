import os
from dotenv import load_dotenv
import json
import requests
import datetime

# Load environment variables from .env file
load_dotenv()

# Get environment variables
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
SHEETY_USERNAME = os.environ.get("SHEETY_USERNAME")
SHEETY_PROJECT_NAME = os.environ.get("SHEETY_PROJECT_NAME")
SHEETY_SHEET_NAME = os.environ.get("SHEETY_SHEET_NAME")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")


# Function to read and increment the object ID from JSON file
def increment_object_id():
    with open("object_id.json", "r+") as file:
        data = json.load(file)
        current_object_id = data["object_id"]
        updated_object_id = current_object_id + 1
        data["object_id"] = updated_object_id
        file.seek(0)
        json.dump(data, file, indent=4)
    return updated_object_id


# Get the current object ID
OBJECT_ID = increment_object_id()

# Get the current date and time
date = datetime.date.today().strftime("%Y-%m-%d")
time = datetime.datetime.now().strftime("%H:%M:%S")

# Prepare the date and time dictionary
datetime_dict = {
    'date': date,
    'time': time
}

nutrition_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

nutrition_headers = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

# Collect exercise data from the user
query = input("Which exercise you did today?: ")

nutrition_parameters = {
    "query": query
}

response = requests.post(url=nutrition_endpoint, headers=nutrition_headers, json=nutrition_parameters)

nutrition_data = response.json()

# Prepare the nutrition dictionary
nutrition_dict = {
    'exercise': nutrition_data['exercises'][0]['user_input'],
    'duration': nutrition_data['exercises'][0]['duration_min'],
    'calories': nutrition_data['exercises'][0]['nf_calories']
}

# Merge datetime_dict and nutrition_dict into a single dictionary
workout_data = {
    'workout': {
        **datetime_dict,
        **nutrition_dict
    }
}

# Ensure the endpoint URL structure matches the required format
sheety_endpoint = f"https://api.sheety.co/{SHEETY_PROJECT_NAME}/{SHEETY_SHEET_NAME}/{OBJECT_ID}"

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}",
    "Content-Type": "application/json"
}

# Print the payload being sent to Sheety for debugging
print("Payload to Sheety:")
print(workout_data)

# Send the merged data to Sheety using PUT request
sheety_response = requests.put(url=sheety_endpoint, json=workout_data, headers=sheety_headers)

# Print the response for debugging
print("Sheety Response Status Code:", sheety_response.status_code)
print("Sheety Response JSON:", sheety_response.json())
