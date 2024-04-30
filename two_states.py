import streamlit as st
import requests
import sys
sys.path.append('D:\\Download')
from DataBase_Countries import get_country_code, country_codes

def run_visa_checker():
    st.title('Visa Requirement Checker')

    departure_country = st.selectbox("Select your departure country:", [""] + list(country_codes.values()), key='two_states_departure_country')
    destination_country = st.selectbox("Select your destination country:", [""] + list(country_codes.values()), key='two_states_destination_country')

    #get the names of the country codes
    departure_code = get_country_code(departure_country) if departure_country else None
    destination_code = get_country_code(destination_country) if destination_country else None

    #print visa requirements between the two (visa-free, visa on arrival, visa required, covid-ban, no admission)
    if st.button('Check Visa Requirement') and departure_code and destination_code:
        url = f'https://rough-sun-2523.fly.dev/api/{departure_code}/{destination_code}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'VF' in data.get('status', ''):
                duration = data.get('dur', None)
                if duration:
                    st.success(f'A visa is not required up until {duration} days.')
                else:
                    st.success('A visa is not required.')
            elif 'VOA' in data.get('status', ''):
                st.warning ('You will obtain a visa upon arrival.')
            elif 'VR' in data.get ('status', ''):
                st.error ('A visa is required')
            elif 'CB' in data.get ('status', ''):
                st.error ('Travel is currently banned due to Covid-19 restrictions.')
            elif 'NA' in data.get ('status', ''):
                st.error ('No entry is permitted to travelers from your country.')
            else:
                st.warning('The visa requirement for your destination is not clear or is unspecified.')
        else:
            st.error(f"Failed to retrieve data. Status code: {response.status_code}")
run_visa_checker()

