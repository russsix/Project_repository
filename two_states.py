import streamlit as st
import requests
from DataBase_Countries import get_country_code

def run_visa_checker():
    st.title('Visa Requirement Checker')

    departure_country = st.text_input("Enter your departure country:", key='departure_country').strip()
    destination_country = st.text_input("Enter your destination country:", key='destination_country').strip()

    departure_code = get_country_code(departure_country)
    destination_code = get_country_code(destination_country)

    if departure_country and not departure_code:
        st.error(f"'{departure_country}' is not recognized. Please enter a valid country name.")
    if destination_country and not destination_code:
        st.error(f"'{destination_country}' is not recognized. Please enter a valid country name.")

    if departure_code and destination_code:
        if st.button('Check Visa Requirement'):
            url = f'https://rough-sun-2523.fly.dev/api/{departure_code}/{destination_code}'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                process_visa_data(data)
            else:
                st.error(f"Failed to retrieve data. Status code: {response.status_code}")

def process_visa_data(data):
    status = data.get('status', '').upper()
    if 'VF' in status:
        duration = data.get('dur', None)
        if duration:
            st.success(f'A visa is not required up until {duration} days.')
        else:
            st.success('A visa is not required.')
    elif 'VOA' in status:
        st.warning('You need to obtain a visa upon arrival.')
    elif 'VR' in status:
        st.error('A visa is required')
    elif 'CB' in status:
        st.error('Travel is currently banned due to Covid-19 restrictions.')
    elif 'NA' in status:
        st.error('No entry is permitted to travelers from your country.')
    else:
        st.warning('The visa requirement for your destination is not clear or is unspecified.')

run_visa_checker()
