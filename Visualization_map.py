import streamlit as st
import requests
from DataBase_Countries import get_country_code, get_country_name
import folium

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
            if data:
                # ... (Code for displaying visa information as per the existing code)

                # Create a map to visualize visa-free and visa-required countries
                visa_map = folium.Map(location=[0, 0], zoom_start=2)

                # Add markers for visa-free countries (green) and visa-required countries (red)
                for code in data.get('vf', {}).get('data', []):
                    country_name = get_country_name(code)
                    folium.Marker(location=get_country_coordinates(country_name), popup=country_name, icon=folium.Icon(color='green', icon='info-sign')).add_to(visa_map)

                for code in data.get('vr', {}).get('data', []):
                    country_name = get_country_name(code)
                    folium.Marker(location=get_country_coordinates(country_name), popup=country_name, icon=folium.Icon(color='red', icon='info-sign')).add_to(visa_map)
                
                # Display the map
                st.write("Visa Status Map")
                st.write(visa_map._repr_html_(), unsafe_allow_html=True)
            else:
                st.error("No visa information available for the selected country.")
        else:
            st.error(f"Failed to retrieve data. Status code: {response.status_code}")

def get_country_coordinates(country_name):
    # Add logic to fetch the coordinates of the given country (e.g., using a geocoding service or a predefined database)
    # Return the latitude and longitude of the country
    return [latitude, longitude]  # Replace with actual coordinates

run_visa_checker()

