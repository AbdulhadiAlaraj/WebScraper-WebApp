# streamlit_app.py
import streamlit as st
import requests

# Streamlit Page Configuration
st.set_page_config(page_title="Web Scraper", page_icon="🌐")

# Title and Introduction
st.title("Web Scraper Application")
st.write("Enter the details for the web page you want to scrape:")

# Input form
with st.form(key='scraper_form'):
    url = st.text_input("Start URL")
    match_pattern = st.text_input("Match Pattern")
    selector = st.text_input("CSS Selector")
    max_pages = st.number_input("Max Pages to Crawl", value=10)
    output_file = st.text_input("Output File Name", value="output.json")
    submit_button = st.form_submit_button("Start Scraping")

# On form submission - send data to the FastAPI backend
if submit_button:
    scraper_config = {
        "url": url,
        "match": match_pattern,
        "selector": selector,
        "maxPagesToCrawl": int(max_pages),
        "outputFileName": output_file
    }
    
    # Send a request to the FastAPI server
    response = requests.post("http://fastapi:8000/start_scraping/", json=scraper_config)
    
    # response = requests.post("http://localhost:8000/start_scraping/", json=scraper_config)
    
    if response.status_code == 200:
        st.success("Scraping initiated! Check server logs or output file.")
    else:
        st.error(f"Failed to initiate scraping: {response.text}")
