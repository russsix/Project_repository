import streamlit as st
import requests

from DataBase_Countries import get_country_code, country_codes
from one_state import run_visa_country_status

def run_visa_checker():
    st.title('Visa Requirement Checker')

    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'home'

    # Define navigation function
    def navigate_to(page_name):
        st.session_state.current_page = page_name

    departure_country = st.selectbox("Select your passport country:", [""] + list(country_codes.keys()), key='checker_departure_country')
    destination_country = st.selectbox("Select your destination country:", [""] + list(country_codes.keys()), key='checker_destination_country')

    if st.button('Check Visa Requirement'):
        departure_code = get_country_code(departure_country) if departure_country else None
        destination_code = get_country_code(destination_country) if destination_country else None
        url = f'https://rough-sun-2523.fly.dev/api/{departure_code}/{destination_code}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            visa_status = data.get('status', '')
            st.session_state.visa_status = visa_status  # Save visa status to session state
            st.session_state.response_data = data  # Save response data to session state
            navigate_to('result')  # Switch to results page
        else:
            st.error(f"Failed to retrieve data. Status code: {response.status_code}")

    # Page handling
    if st.session_state.current_page == 'home':
        st.write("Welcome to the Visa Requirement Checker. Please select your countries and check visa requirements.")
    elif st.session_state.current_page == 'result':
        visa_status = st.session_state.get('visa_status', '')
        data = st.session_state.get('response_data', {})
        # Display visa status results
        if visa_status == 'VF':
            duration = data.get('dur', None)
            message = f'A visa is not required up until {duration} days.' if duration else 'A visa is not required.'
            st.success(message)
        elif visa_status == 'VOA':
            st.warning('You will obtain a visa upon arrival.')
        elif visa_status == 'VR':
            st.error('A visa is required.')
            if st.button("See Visa-Free Destinations"):
                navigate_to('visa_free_destinations')
        elif visa_status == 'CB':
            st.error('Travel is currently banned due to Covid-19 restrictions.')
        elif visa_status == 'NA':
            st.error('No entry is permitted to travelers from your country.')
        else:
            st.warning('The visa requirement for your destination is not clear or is unspecified.')

    if st.session_state.current_page == 'visa_free_destinations':
        run_visa_country_status()

if __name__ == "__main__":
    run_visa_checker()
