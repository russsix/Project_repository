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

def color_for_visa_status(country, visa_data):
    """Assign color based on visa requirement status."""
    visa_required_countries = [get_country_name(code) for code in visa_data.get('vr', {}).get('data', [])]
    visa_on_arrival_countries = [get_country_name(code) for code in visa_data.get('voa', {}).get('data', [])]
    visa_free_countries = [get_country_name(code) for code in visa_data.get('vf', {}).get('data', [])]

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

    # Use 'ADMIN' as the country name column in your GeoDataFrame
    world['color'] = world['ADMIN'].apply(lambda x: color_for_visa_status(x, visa_data))

    fig, ax = plt.subplots(1, figsize=(15, 10))
    world.plot(ax=ax, color=world['color'], linewidth=0.5, edgecolor='black')
    ax.set_facecolor('none')  # Set background to transparent
    ax.axis('off')
    ax.set_title('World Map by Visa Requirement Status')

    fig.patch.set_facecolor('none')
    fig.patch.set_alpha(0)

    # Make the axis background transparent
    ax.patch.set_facecolor('none')
    
    st.pyplot(fig)

def run_visa_country_status():
    st.title('Visa Country Status')
    selected_country = st.selectbox('Select your passport country:', list(country_codes.keys()))
    passport_code = get_country_code(selected_country)

    if st.button('Show Visa Requirements Map'):
        data = fetch_visa_status_data(passport_code)
        if data:
            plot_map(data)
        else:
            st.error("No visa data available for the selected country.")

run_visa_country_status()
