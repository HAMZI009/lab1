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

def main():
    st.title("Wikipedia Web Scraper")
    url = st.text_input("Enter the Wikipedia URL:", "https://en.wikipedia.org/wiki/Lahore")
    if st.button("Scrape"):
        title, text = scrape_wikipedia(url)
        if title and text:
            st.header(title)
            st.write(text)
        else:
            st.error("Failed to scrape the webpage.")

if __name__ == '__main__':
    main()
