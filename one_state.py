import streamlit as st
import requests
import geopandas as gpd
import plotly.express as px
import sys
import pandas as pd

sys.path.append('rachelemantero/Project_repository/')
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
    covid_ban_countries = [get_country_name(code) for code in visa_data.get('covid_ban', {}).get('data', [])]
    no_admission_countries = [get_country_name(code) for code in visa_data.get('no_admission', {}).get('data', [])]

    if country in covid_ban_countries:
        return 'COVID-19 Ban'
    elif country in no_admission_countries:
        return 'No Admission'
    elif country in visa_required_countries:
        return 'Visa Required'
    elif country in visa_on_arrival_countries:
        return 'Visa On Arrival'
    elif country in visa_free_countries:
        return 'Visa Free'
    else:
        return 'Unknown'

def plot_map(visa_data):
    """Plot the world map with countries colored based on visa requirement status."""
    world = gpd.read_file("rachelemantero/Project_repository/global_states.geojson") 
    world['Visa Status'] = world['ADMIN'].apply(lambda x: color_for_visa_status(x, visa_data))

    # Ensure the ordering of 'Visa Status' categories
    category_order = ['Visa Required', 'Visa On Arrival', 'Visa Free', 'COVID-19 Ban', 'No Admission', 'Unknown']
    world['Visa Status'] = pd.Categorical(world['Visa Status'], categories=category_order, ordered=True)

    # Sort the dataframe by 'Visa Status' to ensure correct legend order
    world.sort_values('Visa Status', inplace=True)
    
    fig = px.choropleth(
        world, 
        geojson=world.geometry, 
        locations=world.index, 
        color='Visa Status',
        color_discrete_map={
            'Visa Required': 'red',
            'Visa On Arrival': 'yellow',
            'Visa Free': 'green',
            'COVID-19 Ban': 'blue',
            'No Admission': 'black',
            'Unknown': 'grey'
        },
        projection='natural earth',
        labels={'Visa Status': 'Visa Requirement Status'},
        title='World Map by Visa Requirement Status',
        hover_name='ADMIN',  # Show country name
        hover_data={'Visa Status': True}  # Include visa status in the hover
    )
    # Update layout for transparent background and no index in hover data
    fig.update_geos(visible=False, bgcolor='rgba(0,0,0,0)')
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        geo=dict(
            landcolor='rgba(0,0,0,0)',
            showland=True,
            showcountries=True,
            countrycolor='white'
        ),
        legend_title_text='Visa Status',
        coloraxis_showscale=True  # Enable the color scale
    )

    st.plotly_chart(fig)

def run_visa_country_status():
    st.title('Visa Country Status')
    
    selected_country = st.selectbox('Select your passport country:', list(country_codes.keys()), key = 'status_selected_country')
    passport_code = get_country_code(selected_country)

    if st.button('Show Visa Requirements Map'):
        data = fetch_visa_status_data(passport_code)
        if data:
            plot_map(data)
        else:
            st.error("No visa data available for the selected country.")

if __name__ == "__main__":
    run_visa_country_status()
