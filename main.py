import streamlit as st
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import func as fn
# Streamlit app interface
# User input for URL

st.title("Webpage Link Extractor")


url = st.text_input("Enter the URL of the webpage:")

if st.button("Extract Links"):
    if url:
        fn.extract_links(url)
    else:
        st.warning("Please enter a valid URL!")
