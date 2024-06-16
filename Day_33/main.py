import requests  # Import the requests module for making HTTP requests

# Send a GET request to the specified URL to get the current position of the ISS
response = requests.get(url="http://api.open-notify.org/iss-now.json")

# Raise an exception if the response status code is not 200 (OK)
response.raise_for_status()

# Convert the response content to JSON format
data = response.json()

# Extract the longitude and latitude from the JSON data representing the ISS position
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

# Create a tuple containing the ISS longitude and latitude
iss_position = (longitude, latitude)

# Print the ISS position (longitude, latitude)
print(iss_position)