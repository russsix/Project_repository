import streamlit as st
import requests
from DataBase_Countries import get_country_code

def run_visa_checker():
    st.title('Visa Requirement Checker')

    # Get user input for departure and destination countries
    departure_country = st.text_input("Enter your departure country:").title().strip()
    destination_country = st.text_input("Enter your destination country:").title().strip()

    # Get the country codes
    departure_code = get_country_code(departure_country)
    destination_code = get_country_code(destination_country)

    # Validate the country names and display appropriate error messages
    if not departure_code and departure_country:
        st.error(f"'{departure_country}' is not recognized. Please enter a valid country name.")
    if not destination_code and destination_country:
        st.error(f"'{destination_country}' is not recognized. Please enter a valid country name.")

    # Button to check visa requirements
    if st.button('Check Visa Requirement') and departure_code and destination_code:
        url = f'https://rough-sun-2523.fly.dev/api/{departure_code}/{destination_code}'
        response = requests.get(url)
        if response.status_code == 200:
            visa_required = 'visa required' in response.json().get('category', '').lower()
            if visa_required:
                st.success('A visa is required.')
            else:
                st.info('A visa is not required.')
        else:
            st.error(f"Failed to retrieve data. Status code: {response.status_code}")
