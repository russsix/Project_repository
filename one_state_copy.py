import streamlit as st
import requests
from DataBase_Countries import get_country_code

def run_visa_checker():
    st.title('Visa Country Status')

    departure_country = st.text_input("Enter your departure country:", key='departure_country')

    departure_code = get_country_code(departure_country) if departure_country else None
    
    if departure_country and not departure_code:
        st.error(f"'{departure_country}' is not recognized. Please enter a valid country name.")

    if st.button('Visa Country Status') and departure_code:
        url = f'https://rough-sun-2523.fly.dev/api/{departure_code}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
        else:
            st.error(f"Failed to retrieve data. Status code: {response.status_code}")
run_visa_checker()

