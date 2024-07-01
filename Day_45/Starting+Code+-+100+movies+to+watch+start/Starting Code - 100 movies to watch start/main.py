import requests  # Import the requests library to handle HTTP requests
from bs4 import BeautifulSoup  # Import BeautifulSoup to parse HTML

# URL of the webpage to be scraped
URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# Send a GET request to the URL and store the response
response = requests.get(URL)

# Get the text content from the response
data = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(data, "html.parser")

# Find all elements with the class "listicleItem_listicle-item__title__BfenH"
titles = soup.findAll(class_="listicleItem_listicle-item__title__BfenH")

# Open a file named "movies.txt" in write mode
with open("movies.txt", "w") as file:
    # Loop through the titles in reverse order
    for title in reversed(titles):
        # Write each title text to the file, followed by a newline
        file.write(title.text + "\n")
