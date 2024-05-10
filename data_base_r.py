import requests
import streamlit as st
from DataBase_Countries import country_codes

@st.cache  # Cache the results of this function to avoid refetching from API on every reload
def fetch_visa_free_counts():
    visa_free_counts = {}
    for name, code in country_codes.items():
        url = f'https://rough-sun-2523.fly.dev/api/{code}'
        response = requests.get(url)
        data = response.json()
        visa_free_counts[code] = len(data.get('vf', {}).get('data', []))
    return visa_free_counts

# Fetch and cache visa-free counts for all countries
all_visa_free_counts = fetch_visa_free_counts()

# Sort countries by the number of visa-free countries in descending order
sorted_visa_free_counts = sorted(all_visa_free_counts.items(), key=lambda item: item[1], reverse=True)

# Displaying the sorted list
st.write(sorted_visa_free_counts)
st.write('Hey')
