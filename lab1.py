import requests
from bs4 import BeautifulSoup
import streamlit as st

# Define the URL to scrape
url = 'https://en.wikipedia.org/wiki/Lahore'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the main heading of the Wikipedia page
main_heading = soup.find(id='firstHeading').text

# Display the main heading using Streamlit
st.title(main_heading)
