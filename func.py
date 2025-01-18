import streamlit as st
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
# extract links to fetch and parse links from a webpage
def extract_links(url):
    response = requests.get(url)

    # if extracted
    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')

        links = soup.find_all('a', href=True)

        # Filter out unwanted/dummy links
        valid_links = [link for link in links if not link['href'].startswith(('javascript:', '#'))]

        # total number of valid links
        st.write(f"### Total number of valid links found: {len(valid_links)}")

        # Deploy all valid URLs using streamlit
        for i, link in enumerate(valid_links, 1):
            href = link['href']
            st.write(f"**{i}. Original link:** {href}")
            st.write(f"({urljoin(url, href)})")
            st.markdown("---")
    else:
        st.error(f"Failed to retrieve the webpage. Status code: {response.status_code}") ## if not extracted
