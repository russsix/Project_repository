import streamlit as st
import requests
from DataBase_Countries import get_country_code

def run_visa_checker():
    st.title('Visa Requirement Checker')

    # Get user input for departure and destination countries
    departure_country = st.text_input("Enter your departure country:").title().strip()
    destination_country = st.text_input("Enter your destination country:").title().strip()

    # Get the country codes
    departure_code = get_country_code(departure_country) if departure_country else None
    destination_code = get_country_code(destination_country) if destination_country else None

    # Validate the country names and display appropriate error messages
    if departure_country and not departure_code:
        st.error(f"'{departure_country}' is not recognized. Please enter a valid country name.")
    if destination_country and not destination_code:
        st.error(f"'{destination_country}' is not recognized. Please enter a valid country name.")

    # Button to check visa requirements
    if st.button('Check Visa Requirement') and departure_code and destination_code:
        # Use the country codes to make the API request
        url = f'https://rough-sun-2523.fly.dev/api/{departure_code}/{destination_code}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            visa_required = 'visa required' in data.get('category', '').lower()
            if visa_required:
                st.success('A visa is required.')
            else:
                st.info('A visa is not required.')
        else:
            st.error(f"Failed to retrieve data. Status code: {response.status_code}")
