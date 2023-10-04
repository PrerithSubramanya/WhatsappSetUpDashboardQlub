# Whatsapp Notification Setup Dashboard

This project provides a simple Streamlit dashboard that fetches contact group name and id from an API, and allows users to search for group names using fuzzy string matching.

## Installation

1. Clone this repository:
```
git clone [your-repo-url]
```

2. Navigate to the repository's directory:
```
cd [your-repo-directory]
```

3. Install the required packages:
```
pip install streamlit fuzzywuzzy python-Levenshtein requests
```

## Usage

1. Run the Streamlit app:
```
streamlit run app.py
```

2. Open the provided link in your browser.

3. Use the search box to enter a contact name and click the "Search" button to find the best matching contact.

## Features

- **API Data Fetching**: Retrieves contact data from the API and caches it in memory.
- **Fuzzy Search**: Uses fuzzy string matching to find the best match for the entered search term.
- **Interactive UI**: Provides an intuitive and user-friendly interface.

