import requests
from DataBase_Countries import country_codes
import streamlit as st

def fetch_visa_free_count(country_code):
    url = f'https://rough-sun-2523.fly.dev/api/{country_code}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if not data.get('error', {}).get('status', True):  # Checking if there's no error
            return len(data.get('vf', {}).get('data', []))
    return 0  # Return 0 if there's an error or no data

def get_country_code(country_name):
    return country_codes.get(country_name)

# Dictionary to store the number of visa-free countries per code
visa_free_counts = {}

# Fetch visa-free counts for each country code
for name, code in country_codes.items():
    visa_free_counts[name] = fetch_visa_free_count(code)  # Changed index to name for better readability

# Sort countries by the number of visa-free countries in descending order
sorted_visa_free_counts = sorted(visa_free_counts.items(), key=lambda item: item[1], reverse=True)

# Displaying the sorted list in a nicer format
st.write("Visa-Free Access Count by Country:")
st.dataframe(sorted_visa_free_counts, width=500, height=400)  # Using a DataFrame for better UI presentation

selected_country = st.selectbox('Select your passport country:', list(country_codes.keys()), key='status_selected_country')
country_code = get_country_code(selected_country)

# Optionally display details for the selected country
if st.button('Show Visa-Free Details'):
    visa_free_count = fetch_visa_free_count(country_code)
    st.write(f'{selected_country} has visa-free access to {visa_free_count} countries.')
