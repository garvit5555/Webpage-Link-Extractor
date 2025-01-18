import streamlit as st
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# extract links to fetch and parse links from a webpage
def extract_links(url):
    try:
        response = requests.get(url)

        # if extracted
        if response.status_code == 200:

            soup = BeautifulSoup(response.text, 'html.parser')

            links = soup.find_all('a', href=True)

            # Filter out unwanted/dummy links
            valid_links = [link for link in links if not link['href'].startswith(('javascript:', '#'))]

            #firstly extract the domain of the entered URL
            base_domain = urlparse(url).netloc

            # we will be taking the links that belongs only to the domain of entered URL
            same_domain_links = [link for link in valid_links if urlparse(urljoin(url, link['href'])).netloc == base_domain]

            # total number of valid links
            st.write(f"### Total number of valid links found: {len(same_domain_links)}")

            # Display all valid URLs using Streamlit
            for i, link in enumerate(same_domain_links, 1):
                href = link['href']
                full_url = urljoin(url, href)
                st.write(f"**{i}. Original link:** {href}")
                st.write(f"({full_url})")
                st.markdown("---")
        else:
            st.error(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# end
