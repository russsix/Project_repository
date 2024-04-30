import streamlit as st
import requests
import geopandas as gpd
import matplotlib.pyplot as plt
from DataBase_Countries import get_country_code, get_country_name
from one_state_copy import run_visa_country_status

# Set up Streamlit
st.title('World Map by Visa Requirement Status')

# User selects a country
def visa_map ()
    run_visa_country_status ()

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

