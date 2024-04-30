import streamlit as st
import requests
import geopandas as gpd
import matplotlib.pyplot as plt
from DataBase_Countries import get_country_code, get_country_name


# Set up Streamlit
st.title('Visa Requirement Information')

# User selects a country
country_list = ['Switzerland, Italy']  # Update with actual list of countries
selected_country = st.selectbox('Select your passport country:', country_list)

if selected_country:
    passport_code = get_country_code(selected_country)

    # Request visa information from the API
    url = f'https://rough-sun-2523.fly.dev/api/{passport_code}'
    response = requests.get(url)
    data = response.json()

    # Prepare lists of countries based on visa requirement
    visa_required_countries = [get_country_name(code) for code in data.get('vr', {}).get('data', [])]
    visa_on_arrival_countries = [get_country_name(code) for code in data.get('voa', {}).get('data', [])]
    visa_free_countries = [get_country_name(code) for code in data.get('vf', {}).get('data', [])]

    # Load geographical data from the GeoJSON file
    geo_df = gpd.read_file("D:\\Download\\global_states.geojson")

    # Define a function to return the color based on the visa status
    def color_for_visa_status(country):
        if country in visa_required_countries:
            return 'red'
        elif country in visa_on_arrival_countries:
            return 'yellow'
        elif country in visa_free_countries:
            return 'green'
        else:
            return 'grey'  # Default color if status is unknown

    # Apply the color to each country using the function
    geo_df['color'] = geo_df['ADMIN'].apply(color_for_visa_status)

    # Plot the GeoDataFrame
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    geo_df.plot(ax=ax, color=geo_df['color'])

    # Remove axis for a cleaner look
    ax.axis('off')

    # Set a title for the map
    ax.set_title('World Map by Visa Requirement Status')

    # Show the plot using Streamlit
    st.pyplot(fig)

