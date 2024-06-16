import requests  # Import the requests library to make HTTP requests

# Define the parameters for the API request
parameters = {
    "amount": 10,  # Number of trivia questions to retrieve
    "type": "boolean",  # Type of questions (True/False)
    "category": 18,  # Category of questions (18 corresponds to Science: Computers)
}

# Make a GET request to the Open Trivia Database API with the specified parameters
response = requests.get(url="https://opentdb.com/api.php", params=parameters)

# Raise an HTTPError if the HTTP request returned an unsuccessful status code
response.raise_for_status()

# Parse the JSON response into a Python dictionary
data = response.json()

# Extract the list of trivia questions from the response data
question_data = data["results"]
