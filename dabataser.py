import requests
import streamlit as st

# Assuming 'country_codes' is your dictionary of countries
country_codes = {"Switzerland": "CH", "Italy": "IT", "Germany": "DE", "Afghanistan":"AF"}
    # "CountryName": "CountryCode",
    # Add your complete country codes dictionary here


def fetch_visa_free_count(country_code):
    url = f'https://rough-sun-2523.fly.dev/api/{country_code}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if not data.get('error', {}).get('status', True):  # Checking if there's no error
            return len(data.get('vf', {}).get('data', []))
    return 0  # Return 0 if there's an error or no data

# Dictionary to store the number of visa-free countries per code
visa_free_counts = {}

# Fetch visa-free counts for each country code
for name, code in country_codes.items():
    visa_free_counts[code] = fetch_visa_free_count(code)

# Sort countries by the number of visa-free countries in descending order
sorted_visa_free_counts = sorted(visa_free_counts.items(), key=lambda item: item[1], reverse=True)

# Print the sorted list
st.write(sorted_visa_free_counts)