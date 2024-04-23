import streamlit as st
import requests
from DataBase_Countries import get_country_code



def destinations(passport_country):
    api_url = f'https://rough-sun-2523.fly.dev/api/{passport_country}'
    response = requests.get(api_url)
    
    if response.status_code == 200:
        visa_free_destinations = response.json()
        if isinstance(visa_free_destinations, list):
            for dest in visa_free_destinations:
                for key, val in dest.items():
                    if key in Data_Object_Type:
                        dest[key] = Data_Object_Type[key](val)
            return visa_free_destinations
    return []

def main():
    st.title("Visa-Free Travel Destinations")
    passport_country = st.text_input("Enter your passport country: ")
    if st.button("Search"):
        visa_free_destinations = get_visa_free_destinations(passport_country)
        if visa_free_destinations:
            st.write(f"Visa-Free travel destinations for {passport_country}:")
            for destination_country in visa_free_destinations:
                st.write(destination_country)
        else:
            st.write("No visa-free travel destinations found.")

if __name__ == "__main__":
    main()
