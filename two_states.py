import streamlit as st
import requests

from DataBase_Countries import get_country_code, country_codes, get_country_name

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
        if departure_code and destination_code:
            url = f'https://rough-sun-2523.fly.dev/api/{departure_code}/{destination_code}'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                visa_status = data.get('status', '')
                st.session_state.visa_status = visa_status  # Save visa status to session state
                st.session_state.departure_code = departure_code  # Save departure code for later use
                navigate_to('result')  # Switch to results page
            else:
                st.error(f"Failed to retrieve data. Status code: {response.status_code}")

    # Handle home page display
    if st.session_state.current_page == 'home':
        st.write("Welcome to the Visa Requirement Checker. Please select your countries and check visa requirements.")

    # Handle result display and navigation to visa-free destinations
    elif st.session_state.current_page == 'result':
        handle_visa_result()

    # Display only visa-free destinations if navigated to this page
    elif st.session_state.current_page == 'visa_free_destinations':
        display_visa_free_destinations(st.session_state.departure_code)

def handle_visa_result():
    visa_status = st.session_state.get('visa_status', '')
    if visa_status == 'VF':
        duration = st.session_state.response_data.get('dur', None)
        message = f'A visa is not required up until {duration} days.' if duration else 'A visa is not required.'
        st.success(message)
    elif visa_status == 'VOA':
        st.warning('You will obtain a visa upon arrival.')
    elif visa_status == 'VR':
        st.error('A visa is required.')
        st.write ('Is this not what you were expecting? To see al your visa-free destinations click the button below.')
        if st.button("See Visa-Free Destinations"):
            st.session_state.current_page = 'visa_free_destinations'
    elif visa_status == 'CB':
        st.error('Travel is currently banned due to Covid-19 restrictions.')
    elif visa_status == 'NA':
        st.error('No entry is permitted to travelers from your country.')
    else:
        st.warning('The visa requirement for your destination is not clear or is unspecified.')

def display_visa_free_destinations(departure_code):
    url = f'https://rough-sun-2523.fly.dev/api/{departure_code}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        visa_free_countries = [get_country_name(code) for code in data.get('vf', {}).get('data', [])]
        if visa_free_countries:
            # Join all country names into a single string with each name on a new line
            formatted_countries = ", ".join(visa_free_countries)
            st.write(formatted_countries)  # Using st.text to maintain text format without additional styling
        else:
            st.write("No visa-free destinations available.")
    else:
        st.error("Failed to retrieve visa-free destinations.")

if __name__ == "__main__":
    run_visa_checker()
