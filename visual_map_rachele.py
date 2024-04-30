import streamlit as st
import requests
import geopandas as gpd
import matplotlib.pyplot as plt
import sys
from streamlit_bokeh_events import streamlit_bokeh_events
from bokeh.plotting import figure

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

    # Create a Bokeh figure
    p = figure(width=800, height=600, toolbar_location=None, tools="")
    p.axis.visible = False

    # Add polygons for each country
    for country, geometry in zip(world['ADMIN'], world['geometry']):
        x, y = geometry.exterior.xy
        p.patches([x], [y], fill_color=color_for_visa_status(country, visa_data), line_color="black")

    # Add hover tool to display country names
    hover = p.hover
    hover.tooltips = [("Country", "@country")]
    hover.point_policy = "follow_mouse"

    # Add country names as text annotations
    for country, geometry in zip(world['ADMIN'], world['geometry']):
        centroid = geometry.centroid
        p.text(x=[centroid.x], y=[centroid.y], text=[country], text_font_size="8pt", text_align="center", text_baseline="middle", text_color="black", text_alpha=0)

    # Add zoom event handler
    event_result = streamlit_bokeh_events(bokeh_plot=p, events="PAN", key="pan")
    if event_result:
        # If a pan event occurs (zoom in), show country names
        p.text_alpha = 1
    else:
        # Otherwise, hide country names
        p.text_alpha = 0

    # Show the Bokeh plot
    st.bokeh_chart(p)

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
