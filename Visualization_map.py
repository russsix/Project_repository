import streamlit as st
import folium
import requests
from DataBase_Countries import get_country_code, get_country_name
from one_state_copy import run_visa_country_status


run_visa_status()

# Create a base map
m = folium.Map(location=[0, 0], zoom_start=2)

# Function to determine color based on whether the country is selected or not
def get_color(country):
    if country in st:
        return 'green'
    else:
        return 'red'

# Add countries to the map
for country in contries:
    folium.CircleMarker(
        location=[0, 0],
        radius=5,
        color=get_color(country),
        fill=True,
        fill_color=get_color(country),
        fill_opacity=0.7,
        tooltip=country
    ).add_to(m)

# Display the map
st.markdown(m._repr_html_(), unsafe_allow_html=True)
