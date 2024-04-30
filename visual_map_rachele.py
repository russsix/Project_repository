import streamlit as st
import requests
import geopandas as gpd
import matplotlib.pyplot as plt
import sys

sys.path.append('D:\\Download')
from DataBase_Countries import country_codes, get_country_code, get_country_name

def fetch_visa_status_data(passport_code):
    """Fetch visa status data from the API."""
    url = f'https://rough-sun-2523.fly.dev/api/{passport_code}'
    response = requests.get(url)
    data = response.json()
    return data

visa_required_countries = [get_country_name(code) for code in data.get('vr', {}).get('data', [])]
visa_on_arrival_countries = [get_country_name(code) for code in data.get('voa', {}).get('data', [])]
visa_free_countries = [get_country_name(code) for code in data.get('vf', {}).get('data', [])]

def color_for_visa_status(country):
    if country in visa_required_countries:
        return 'red'
    elif country in visa_on_arrival_countries:
        return 'yellow'
    elif country in visa_free_countries:
        return 'green'
    else:
        return 'grey'  

def plot_map(visa_data):
    """Plot the world map with countries colored based on visa requirement status."""
    world = gpd.read_file("D:\\Download\\global_states.geojson")

    # Use 'ADM0_A3' as the country code column in your GeoDataFrame
    world['color'] = world['ADMIN'].apply(color_for_visa_status)

    fig, ax = plt.subplots(1, figsize=(15, 10))
    world.plot(ax=ax, color=world['color'], linewidth=0.5, edgecolor='black')
    ax.set_facecolor('none')  # Set background to transparent
    ax.axis('off')
    ax.set_title('World Map by Visa Requirement Status')
    st.pyplot(fig)

def run_visa_country_status():
    st.title('Visa Country Status')
    selected_country = st.selectbox('Select your passport country:', list(country_codes.keys()))
    passport_code = get_country_code(selected_country)

    if st.button('Show Visa Requirements Map'):
        data = fetch_visa_status_data(passport_code)
        if data:
            # Prepare visa data dictionary with ISO codes as keys and visa status as values
            visa_data = {code: status for status, codes in data.items() for code in codes}
            plot_map(visa_data)
        else:
            st.error("No visa data available for the selected country.")

run_visa_country_status()
