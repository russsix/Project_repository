import streamlit as st
import requests
from DataBase_Countries import get_country_code

def run_visa_checker():
    st.title('Visa Requirement Checker')

    departure_country = st.text_input("Enter your departure country:", key='departure_country')
    destination_country = st.text_input("Enter your destination country:", key='destination_country')

    departure_code = get_country_code(departure_country) if departure_country else None
    destination_code = get_country_code(destination_country) if destination_country else None

    if departure_country and not departure_code:
        st.error(f"'{departure_country}' is not recognized. Please enter a valid country name.")
    if destination_country and not destination_code:
        st.error(f"'{destination_country}' is not recognized. Please enter a valid country name.")

    if st.button('Check Visa Requirement') and departure_code and destination_code:
        url = f'https://rough-sun-2523.fly.dev/api/{departure_code}/{destination_code}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'VF' in data.get('status', ''):
                if '' in data.get('dur', ''):
                    st.success('A visa is not required.')
                else:
                    duration = data.get('dur', '')
                    st.success('A visa is not required up until {duration} days.')
            elif 'VOA' in data.get('status', ''):
                st.warning ('You need to obtain a visa upon arrival.')
            elif 'VR' in data.get ('status', ''):
                st.error ('A visa is required')
            elif 'CB' in data.get ('status', ''):
                st.error ('Travel is currently banned due to Covid-19 restrictions.')
            elif 'NO' in data.get ('status', ''):
                st.error ('No entry is permitted to travelers from your country.')
            else:
                st.warning('The visa requirement for your destination is not clear or is unspecified.')
        else:
            st.error(f"Failed to retrieve data. Status code: {response.status_code}")
run_visa_checker()

