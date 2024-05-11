import streamlit as st
import requests

from DataBase_Countries import country_codes, get_country_code, get_country_name

def run_visa_checker():
    st.title('Visa Requirement Checker')

    # Ensure session state variables are initialized
    if 'show_visa_free' not in st.session_state:
        st.session_state.show_visa_free = False
    if 'departure_code' not in st.session_state:
        st.session_state.departure_code = None

    # Input widgets
    departure_country = st.selectbox("Select your passport country:", [""] + list(country_codes.keys()), key='checker_departure_country')
    destination_country = st.selectbox("Select your destination country:", [""] + list(country_codes.keys()), key='checker_destination_country')

    # Handle visa requirement check
    if st.button('Check Visa Requirement'):
        departure_code = get_country_code(departure_country) if departure_country else None
        destination_code = get_country_code(destination_country) if destination_country else None
        if departure_code and destination_code:
            check_visa_requirements(departure_code, destination_code)
        else:
            st.error("Please select both departure and destination countries.")

    # Conditionally display visa-free destinations
    if st.session_state.show_visa_free:
        display_visa_free_destinations()

def check_visa_requirements(departure_code, destination_code):
    st.session_state.departure_code = departure_code  # Store departure code in session state for later use
    url = f'https://rough-sun-2523.fly.dev/api/{departure_code}/{destination_code}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        display_visa_status(data)
    else:
        st.error(f"Failed to retrieve data. Status code: {response.status_code}")

def display_visa_status(data):
    status = data.get('status', '')
    if 'VF' in status:
        duration = data.get('dur', None)
        st.success(f'A visa is not required up until {duration} days.' if duration else 'A visa is not required.')
    elif 'VOA' in status:
        st.warning('You will obtain a visa upon arrival.')
    elif 'VR' in status:
        st.error('A visa is required.')
        st.info('Not what you were expecting? Check out your visa-free destinations.')
        if st.button("See Visa-Free Destinations"):
            st.session_state.show_visa_free = True
    elif 'CB' in status:
        st.error('Travel is currently banned due to Covid-19 restrictions.')
    elif 'NA' in status:
        st.error('No entry is permitted to travelers from your country.')
    else:
        st.warning('The visa requirement for your destination is not clear or is unspecified.')

def display_visa_free_destinations():
    """Fetch and display visa-free destinations using the stored departure code."""
    url = f'https://rough-sun-2523.fly.dev/api/{st.session_state.departure_code}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        visa_free_countries = [get_country_name(code) for code in data.get('vf', {}).get('data', [])]
        st.write("Visa-free destinations:")
        st.write(visa_free_countries)
    else:
        st.error("Failed to retrieve visa-free destinations.")

if __name__ == "__main__":
    run_visa_checker()
