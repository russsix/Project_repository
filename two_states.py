import streamlit as st
import requests
from DataBase_Countries import get_country_code

def run_visa_checker():
    st.title('Visa Requirement Checker')

    departure_country_name = st.text_input("Insert your departure country:", '').title().strip()
    destination_country_name = st.text_input("Insert your destination country:", '').title().strip()

    departure_valid = True
    destination_valid = True

    departure_country_code = get_country_code(departure_country_name) if departure_country_name else None
    destination_country_code = get_country_code(destination_country_name) if destination_country_name else None

    if departure_country_name and not departure_country_code:
        st.error(f"The country '{departure_country_name}' is not recognized. Please enter a valid country name.")
        departure_valid = False

    if destination_country_name and not destination_country_code:
        st.error(f"The country '{destination_country_name}' is not recognized. Please enter a valid country name.")
        destination_valid = False

    if st.button('Check Visa Requirement') and departure_valid and destination_valid:
        if departure_country_code and destination_country_code:
            # Use the country codes in the API request
            url = f'https://rough-sun-2523.fly.dev/api/{departure_country_code}/{destination_country_code}'
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                if 'visa required' in data.get('category', '').lower():
                    st.success('A visa is required.')
                else:
                    st.info('A visa is not required')
            else:
                st.error(f"Failed to retrieve data. Status code: {response.status_code}")