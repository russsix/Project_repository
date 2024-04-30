import streamlit as st
import requests
import geopandas as gpd
import matplotlib.pyplot as plt
import sys
sys.path.append('D:\\Download')
from DataBase_Countries import country_codes, get_country_code, get_country_name

def get_country_color(country_code, visa_data):
    if country_code in visa_data:
        visa_status = visa_data[country_code]
        if visa_status == 'vf':
            return 'green'  # Visa Free
        elif visa_status == 'voa':
            return 'orange'  # Visa on Arrival
        elif visa_status == 'vr':
            return 'red'  # Visa Required
    return 'gray'  # No data

def plot_map(visa_data):
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    world['color'] = world['iso_a3'].apply(lambda x: get_country_color(x, visa_data))
    fig, ax = plt.subplots(figsize=(15, 10))
    world.plot(ax=ax, color=world['color'])
    ax.set_title('Visa Requirements Map')
    ax.set_axis_off()
    st.pyplot(fig)

def run_visa_country_status():
    visa_data = {}
    st.title('Visa Country Status')
    # Use st.selectbox to create a dropdown menu of countries
    passport_country = st.selectbox("Select your departure country:", list(country_codes.keys()))

    passport_code = get_country_code(passport_country) if passport_country else None
    
    if st.button('Show Visa Requirements'):
        if passport_code:
            url = f'https://rough-sun-2523.fly.dev/api/{passport_code}'
            response = requests.get(url)
            data = response.json()
            if data:
                visa_required_countries = [get_country_name(code) for code in data.get('vr', {}).get('data', [])]
                visa_on_arrival_countries = [get_country_name(code) for code in data.get('voa', {}).get('data', [])]
                visa_free_countries = [get_country_name(code) for code in data.get('vf', {}).get('data', [])]
                
                for country_code in visa_required_countries:
                    visa_data[country_code] = 'vr'
                for country_code in visa_on_arrival_countries:
                    visa_data[country_code] = 'voa'
                for country_code in visa_free_countries:
                    visa_data[country_code] = 'vf'
                
                plot_map(visa_data)

                # Display visa status information
                st.write("Visa Required Countries:", ', '.join(visa_required_countries))
                st.write("Visa on Arrival Countries:", ', '.join(visa_on_arrival_countries))
                st.write("Visa Free Countries:", ', '.join(visa_free_countries))
            else:
                st.error("Failed to retrieve visa data. Please try again.")
        else:
            st.error("Invalid country selected. Please choose a valid country from the list.")

run_visa_country_status()
