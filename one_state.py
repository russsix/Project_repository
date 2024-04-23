import streamlit as st
import requests
from DataBase_Countries import get_country_code

Data_Object_Type = {
    "passport": str,
    "VR": str,
    "VOA": str,
    "VF": str,
    "CB": str,
    "NA": str,
    "last_updated": str,
    "error": str,
}

def get_visa_free_destinations(passport_country):
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

passport_country = input("Enter your passport country: ")
visa_free_destinations = get_visa_free_destinations(passport_country)
if visa_free_destinations:
    print(f"Visa-Free travel destinations for {passport_country}:")
    for destination_country in visa_free_destinations:
        print(destination_country)
else:
    print("No visa-free travel destinations found.")
