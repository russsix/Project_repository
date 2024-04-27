import streamlit as st
import pydeck as pdk
import geopandas as gpd

# Load geographical data from the GeoJSON file
geo_data = gpd.read_file(r"D:\Download\global_states.geojson")

# Define the Pydeck layer as a GeoJsonLayer
layer = pdk.Layer(
    "GeoJsonLayer",
    geo_data,
    get_fill_color="[200, 30, 0, 160]",  # Custom fill color
    get_line_color=[0, 0, 0, 255],  # Line color for boundaries
    pickable=True,
    auto_highlight=True,
)

# Set the viewport location to show the whole world
view_state = pdk.ViewState(
    latitude=0,
    longitude=0,
    zoom=1  # You may need to adjust the zoom level
)

# Render the map
st.pydeck_chart(pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    map_style=pdk.map_styles.DARK  # Using a dark theme from Pydeck
))
