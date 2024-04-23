import streamlit as st
import requests

def get_visa_free_destinations(passport_country):
    api_url = f'https://rough-sun-2523.fly.dev/api/{passport_country}'
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None  # or return an empty list depending on what you expect

def main():
    st.title("Visa-Free Travel Destinations")
    passport_country = st.text_input("Enter your passport country: ")
    if st.button("Search"):
        visa_info = get_visa_free_destinations(passport_country)
        if visa_info:
            st.write(f"Visa-Free travel destinations for {passport_country}:")
            st.write("Visa Required:", ', '.join(visa_info['vr']['data']))
            st.write("Visa on Arrival:", ', '.join(visa_info['voa']['data']))
            st.write("Visa Free:", ', '.join(visa_info['vf']['data']))
            if visa_info['cb']['data']:  # Check if list is not empty
                st.write("Covid Ban:", ', '.join(visa_info['cb']['data']))
            if visa_info['na']['data']:  # Check if list is not empty
                st.write("No Admission:", ', '.join(visa_info['na']['data']))
        else:
            st.write("No visa information found or failed to retrieve data.")

if __name__ == "__main__":
    main()
