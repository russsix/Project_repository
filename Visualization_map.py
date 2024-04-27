import streamlit as st
import pydeck as pdk
import geopandas as gpd
import pandas as pd

# Load geographical data from the GeoJSON file
geo_data = gpd.read_file(r"D:\Download\global_states.geojson")

# Define the color for the United States and a default color
us_color = [255, 0, 0, 160]  # Red with some transparency
default_color = [34, 139, 34, 160]  # Dark green with some transparency

# Create a new column 'color' in the GeoDataFrame to store the RGBA values
geo_data['color'] = geo_data.apply(lambda x: us_color if x['ADMIN'] == 'United States of America' else default_color, axis=1).tolist()

# Convert GeoDataFrame to Pydeck data format
geojson = geo_data.__geo_interface__

# Define the Pydeck layer as a GeoJsonLayer using the 'color' column for the fill color
layer = pdk.Layer(
    'GeoJsonLayer',
    geojson,
    opacity=0.8,
    stroked=False,
    filled=True,
    extruded=False,
    get_fill_color='properties.color',
)

# Set the initial view state
view_state = pdk.ViewState(
    latitude=0,  # Center on the US
    longitude=0,
    zoom=1  # Adjust zoom to show the US prominently
)

# Create the deck
deck = pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    map_style='mapbox://styles/mapbox/light-v9'
)

# Render the map in Streamlit
st.pydeck_chart(deck)
