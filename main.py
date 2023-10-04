import streamlit as st
import requests
from fuzzywuzzy import process


API_URL = f"https://api.ultramsg.com/instance47776/contacts?token={st.secrets['API_TOKEN']}"


# Fetch data from the API and store it in memory
def fetch_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        return None


data = fetch_data()

st.title("Whatsapp Notification Dashboard")

if data:
    search_term = st.text_input("Search for a group by name:")
    search_button = st.button("Search")

    if search_button and search_term:
        # Using fuzzy matching to find the best match
        names = [item["name"] for item in data]
        best_match, score = process.extractOne(search_term, names)

        if score > 60:  # You can adjust the threshold as needed
            matched_item = next(item for item in data if item["name"] == best_match)
            st.write(f"Name: {matched_item['name']}, ID: ", matched_item['id'])
        else:
            st.warning("No close matches found for that name.")
else:
    st.error("Failed to fetch data from the API. Please try again later.")


