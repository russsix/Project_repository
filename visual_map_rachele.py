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

def plot_map(visa_data, zoom_level):
    """Plot the world map with countries colored based on visa requirement status."""
    world = gpd.read_file("D:\\Download\\global_states.geojson")

    # Use 'ADMIN' as the country name column in your GeoDataFrame
    world['color'] = world['ADMIN'].apply(lambda x: color_for_visa_status(x, visa_data))

    # Create a new figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the world map with colored countries
    world.plot(ax=ax, color=world['color'], edgecolor='black')

    # Set plot limits based on zoom level
    ax.set_xlim([-180 + zoom_level, 180 - zoom_level])
    ax.set_ylim([-90 + zoom_level, 90 - zoom_level])

    # Hide axes and set title
    ax.axis('off')
    ax.set_title('World Map by Visa Requirement Status')

    # Display country names only when zoomed in
    if zoom_level < 100:
        for _, row in world.iterrows():
            ax.text(row.geometry.centroid.x, row.geometry.centroid.y, row['ADMIN'], fontsize=6, ha='center', va='center')

    # Display the plot
    st.pyplot(fig)

def run_visa_country_status():
    st.title('Visa Country Status')
    selected_country = st.selectbox('Select your passport country:', list(country_codes.keys()))
    passport_code = get_country_code(selected_country)

    zoom_level = st.slider('Zoom Level', min_value=0, max_value=180, value=0, step=10)

    if st.button('Show Visa Requirements Map'):
        data = fetch_visa_status_data(passport_code)
        if data:
            plot_map(data, zoom_level)
        else:
            st.error("No visa data available for the selected country.")

run_visa_country_status()
