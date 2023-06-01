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

def find_badshahi_mosque_info(text):
    info = ""
    sections = text.split("\n\n")
    for section in sections:
        if "Badshahi Mosque" in section or "بادشاہی مسجد" in section:
            info = section
            break
    return info

def main():
    st.title("Badshahi Mosque Wikipedia Scraper")
    url = "https://en.wikipedia.org/wiki/Lahore"
    if st.button("Scrape"):
        title, text = scrape_wikipedia(url)
        if title and text:
            st.header(title)
            badshahi_info = find_badshahi_mosque_info(text)
            if badshahi_info:
                st.subheader("Badshahi Mosque (بادشاہی مسجد)")
                st.write(badshahi_info)
            else:
                st.write("No information about Badshahi Mosque found.")
        else:
            st.error("Failed to scrape the webpage.")

if __name__ == '__main__':
    main()
