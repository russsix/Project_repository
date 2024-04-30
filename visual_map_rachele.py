import streamlit as st
import requests
import geopandas as gpd
import matplotlib.pyplot as plt
from DataBase_Countries import get_country_code
from one_state_copy import run_visa_country_status

# Set up Streamlit
st.title('World Map by Visa Requirement Status')

# Load geographical data from the GeoJSON file
geo_df = gpd.read_file("D:\\Download\\global_states.geojson")

def fetch_visa_status_data(passport_country):
    # Fetch visa status data using the provided function and return lists
    return run_visa_country_status(passport_country)

def visa_map():
    # User selects a country from a dropdown populated with available countries
    country_list = list(geo_df['ADMIN'])  # Example to populate the dropdown with countries from the GeoJSON
    selected_country = st.selectbox('Select your passport country:', country_list)

    # Retrieve visa status data
    visa_required_countries, visa_on_arrival_countries, visa_free_countries, _, _ = fetch_visa_status_data(selected_country)

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

visa_map()
