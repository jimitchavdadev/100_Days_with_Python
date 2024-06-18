import requests
import datetime

# Get the current date in YYYYMMDD format
year = datetime.date.today().year
month = datetime.date.today().month
day = datetime.date.today().day

date = f"{year: 04d}{month: 02d}{day: 02d}"

# Set up user details and token (replace with your own values)
USERNAME = "your_username"
TOKEN = "your_token"

# Define the Pixela endpoint
pixela_endpoint = "https://pixe.la/v1/users"

# Parameters for creating a user (commented out if already created)
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Create user (commented out if already created)
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Define the endpoint for creating a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# Configuration for the graph
graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu"
}

# Headers including the user token
headers = {
    "X-USER-TOKEN": TOKEN
}

# Create graph (commented out if already created)
# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_response.text)

# Define the endpoint for adding/updating pixel data
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
pixel_updation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{date}"

# Configuration for adding pixel data
pixel_config = {
    "date": date,  # Ensure the date is in YYYYMMDD format
    "quantity": "9.71"
}

# Configuration for updating pixel data
update_pixel_config = {
    "quantity": "10.22"
}

# Send a request to delete a pixel data (use other methods for different actions)
pixel_response = requests.delete(url=pixel_updation_endpoint, headers=headers)

# Print the response from the server
print(pixel_response.text)
