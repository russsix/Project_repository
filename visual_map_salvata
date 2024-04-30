import streamlit as st
import requests
import geopandas as gpd
import plotly.express as px
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

def run_visa_country_status():
    st.title('Visa Country Status')
    selected_country = st.selectbox('Select your passport country:', list(country_codes.keys()))
    passport_code = get_country_code(selected_country)

    if st.button('Show Visa Requirements Map'):
        data = fetch_visa_status_data(passport_code)
        if data:
            # Load world map data
            world = gpd.read_file("D:\\Download\\global_states.geojson")

            # Assign color to countries based on visa status
            world['color'] = world['ADMIN'].apply(lambda x: color_for_visa_status(x, data))

            # Plot the world map with Plotly
            fig = px.choropleth(world, 
                                 geojson=world.geometry, 
                                 locations=world.index, 
                                 color='color',
                                 hover_name='ADMIN',  # Country name will be displayed when hovering
                                 projection='natural earth')  # Use natural earth projection for better appearance

            # Update map layout
            fig.update_geos(showcountries=True, 
                            showcoastlines=False, 
                            showland=True, 
                            showocean=True, 
                            showlakes=False, 
                            showrivers=False,
                            fitbounds='locations')

            # Make the background transparent
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',  # Transparent background
                paper_bgcolor='rgba(0,0,0,0)'  # Transparent background
            )

            # Show the plotly figure
            st.plotly_chart(fig)
        else:
            st.error("No visa data available for the selected country.")

run_visa_country_status()
