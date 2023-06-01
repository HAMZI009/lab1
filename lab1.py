import requests
from bs4 import BeautifulSoup
import streamlit as st

def scrape_wikipedia(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('h1').text
        content_div = soup.find(id='mw-content-text')
        paragraphs = content_div.find_all('p')
        text = '\n\n'.join([p.text for p in paragraphs])
        return title, text
    else:
        return None, None

def find_places_cities(text):
    places = []
    cities = []
    
    lines = text.split("\n")
    for line in lines:
        if "tourist attractions" in line.lower():
            if ":" in line:
                start_index = line.index(":") + 1
                places.extend([place.strip() for place in line[start_index:].split(",")])
        if "cities" in line.lower():
            if ":" in line:
                start_index = line.index(":") + 1
                cities.extend([city.strip() for city in line[start_index:].split(",")])

    return places, cities

def main():
    st.title("Wikipedia Places and Cities Scraper")
    url = "https://en.wikipedia.org/wiki/Lahore"
    if st.button("Scrape"):
        title, text = scrape_wikipedia(url)
        if title and text:
            st.header(title)
            places, cities = find_places_cities(text)
            
            if places:
                st.subheader("Tourist Attractions:")
                for place in places:
                    st.write(place)
            
            if cities:
                st.subheader("Cities:")
                for city in cities:
                    st.write(city)
            
            if not places and not cities:
                st.write("No places or cities found.")
        else:
            st.error("Failed to scrape the webpage.")

if __name__ == '__main__':
    main()
