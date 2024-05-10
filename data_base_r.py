import requests
import streamlit as st
from DataBase_Countries import country_codes

def fetch_visa_free_count(country_code):
    url = f'https://rough-sun-2523.fly.dev/api/{country_code}'
    response = requests.get(url)
    data = response.json()
    return len(data.get('vf', {}).get('data', []))
      # Return 0 if there's an error or no data

# Dictionary to store the number of visa-free countries per code
visa_free_counts = {}

# Fetch visa-free counts for each country code
for name, code in country_codes.items():
    visa_free_counts[code] = fetch_visa_free_count(code)

# Sort countries by the number of visa-free countries in descending order
sorted_visa_free_counts = sorted(visa_free_counts.items(), key=lambda item: item[1], reverse=True)

# Print the sorted list
st.write(sorted_visa_free_counts)
st.write ('hey')