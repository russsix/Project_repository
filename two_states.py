import streamlit as st
import requests

from DataBase_Countries import get_country_code, country_codes
from one_state import run_visa_country_status

def run_visa_checker():
    st.title('Visa Requirement Checker')

    # Initialize session state for navigation if not already set
    if 'navigation' not in st.session_state:
        st.session_state.navigation = 'check_visa'

    # Select boxes for choosing countries
    if st.session_state.navigation == 'check_visa':
        departure_country = st.selectbox("Select your passport country:", [""] + list(country_codes.keys()), key='checker_departure_country')
        destination_country = st.selectbox("Select your destination country:", [""] + list(country_codes.keys()), key='checker_destination_country')

        if st.button('Check Visa Requirement'):
            check_visa_requirements(departure_country, destination_country)

    # Function to check visa requirements
    def check_visa_requirements(departure_country, destination_country):
        departure_code = get_country_code(departure_country) if departure_country else None
        destination_code = get_country_code(destination_country) if destination_country else None
        url = f'https://rough-sun-2523.fly.dev/api/{departure_code}/{destination_code}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            show_visa_status(data)
        else:
            st.error(f"Failed to retrieve data. Status code: {response.status_code}")

    # Function to display visa status and handle navigation
    def show_visa_status(data):
        visa_status = data.get('status', '')
        if visa_status == 'VR':
            st.error('A visa is required.')
            if st.button("See Visa-Free Destinations"):
                st.session_state.navigation = 'visa_free_destinations'
        else:
            display_status_message(visa_status, data)

    # Display appropriate messages based on visa status
    def display_status_message(visa_status, data):
        if visa_status == 'VF':
            duration = data.get('dur', None)
            message = f'A visa is not required up until {duration} days.' if duration else 'A visa is not required.'
            st.success(message)
        elif visa_status == 'VOA':
            st.warning('You will obtain a visa upon arrival.')
        elif visa_status == 'CB':
            st.error('Travel is currently banned due to Covid-19 restrictions.')
        elif visa_status == 'NA':
            st.error('No entry is permitted to travelers from your country.')
        else:
            st.warning('The visa requirement for your destination is not clear or is unspecified.')

    # Only display the visa free states function if navigation is set to it
    if st.session_state.navigation == 'visa_free_destinations':
        st.session_state['checker_departure_country'] = None  # Optionally clear previous state
        st.session_state['checker_destination_country'] = None  # Optionally clear previous state
        run_visa_country_status()  # Call the function to display visa-free destinations

if __name__ == "__main__":
    run_visa_checker()
