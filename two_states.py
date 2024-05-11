import streamlit as st
import requests

from DataBase_Countries import get_country_code, country_codes
from one_state import run_visa_country_status


def run_visa_checker():
    st.title('Visa Requirement Checker')

    # Initialize session state variables if they don't exist
    if 'show_visa_free_destinations' not in st.session_state:
        st.session_state.show_visa_free_destinations = False

    departure_country = st.selectbox("Select your passport country:", [""] + list(country_codes.keys()), key='checker_departure_country')
    destination_country = st.selectbox("Select your destination country:", [""] + list(country_codes.keys()), key='checker_destination_country')

    departure_code = get_country_code(departure_country) if departure_country else None
    destination_code = get_country_code(destination_country) if destination_country else None

    if st.button('Check Visa Requirement'):
        url = f'https://rough-sun-2523.fly.dev/api/{departure_code}/{destination_code}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            visa_status = data.get('status', '')
            match visa_status:
                case 'VF':
                    duration = data.get('dur', None)
                    message = f'A visa is not required up until {duration} days.' if duration else 'A visa is not required.'
                    st.success(message)
                case 'VOA':
                    st.warning('You will obtain a visa upon arrival.')
                case 'VR':
                    st.error('A visa is required.')
                    st.info('Not what you were expecting? Check out our "Visa Country Status" feature to see all your visa-free destinations.')
                    if st.button("See Visa-Free Destinations"):
                        st.session_state.show_visa_free_destinations = True
                case 'CB':
                    st.error('Travel is currently banned due to Covid-19 restrictions.')
                case 'NA':
                    st.error('No entry is permitted to travelers from your country.')
                case _:
                    st.warning('The visa requirement for your destination is not clear or is unspecified.')
        else:
            st.error(f"Failed to retrieve data. Status code: {response.status_code}")

    if st.session_state.show_visa_free_destinations:
        run_visa_country_status()

if __name__ == "__main__":
    run_visa_checker()
