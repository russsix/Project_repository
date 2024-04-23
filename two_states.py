import streamlit as st
import requests
from DataBase_Countries import get_country_code

def run_visa_checker():
    st.title('Visa Requirement Checker')
    with st.form("my_form"):
        departure_country = st.text_input("Enter your departure country:", key='departure_country')
        destination_country = st.text_input("Enter your destination country:", key='destination_country')
        submitted = st.form_submit_button("Check Visa Requirement")
    
        if submitted:
            departure_code = get_country_code(departure_country)
            destination_code = get_country_code(destination_country)

            if departure_country and not departure_code:
                st.error(f"'{departure_country}' is not recognized. Please enter a valid country name.")
            if destination_country and not destination_code:
                st.error(f"'{destination_country}' is not recognized. Please enter a valid country name.")

            if departure_code and destination_code:
                url = f'https://rough-sun-2523.fly.dev/api/{departure_code}/{destination_code}'
                response = requests.get(url)
                if response.status_code == 200:
                    data = response.json()
                    visa_required = 'visa required' in data.get('category', '').lower()
                    if visa_required:
                        st.success('A visa is required.')
                    else:
                        st.info('A visa is not required.')
                else:
                    st.error(f"Failed to retrieve data. Status code: {response.status_code}")

