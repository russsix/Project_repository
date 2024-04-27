import streamlit as st
import pydeck as pdk
import geopandas as gpd
import pandas as pd

# Load geographical data from the GeoJSON file
geo_data = gpd.read_file(r"D:\Download\global_states.geojson")

# Initialize a column for colors in hexadecimal, with a default value
default_color = [34, 139, 34, 160]  # Dark green with some transparency
us_color = [255, 0, 0, 160]  # Red with some transparency

# We'll create a new column in the GeoDataFrame for the color
geo_data['color'] = geo_data.apply(
    lambda x: us_color if x['ADMIN'] == 'United States of America' else default_color, axis=1
)

# Convert GeoDataFrame to JSON
geojson = geo_data.__geo_interface__

# Define the Pydeck layer as a GeoJsonLayer
layer = pdk.Layer(
    'GeoJsonLayer',
    geojson,
    stroked=False,
    filled=True,
    extruded=True,
    get_fill_color='color',  # Use 'color' column for the fill color
)

# Set the initial view state
view_state = pdk.ViewState(
    latitude=0, 
    longitude=0, 
    zoom=0
)

# Render the map with the custom colors
r = pdk.Deck(
    layers=[layer], 
    initial_view_state=view_state,
    map_style='mapbox://styles/mapbox/light-v9'
)

st.pydeck_chart(r)
