import sys
st.write(sys.executable)
import streamlit as st
import pydeck as pdk
import geopandas as gpd

# Load geographical data
geo_data = gpd.read_file("path/to/your/global_states.geojson")

# Define the Pydeck layer as a GeoJsonLayer
layer = pdk.Layer(
    "GeoJsonLayer",
    geo_data,
    opacity=0.8,
    stroked=False,
    filled=True,
    extruded=True,
    wireframe=True,
)

# Set the viewport location
view_state = pdk.ViewState(latitude=0, longitude=0, zoom=1)

# Render the map
st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))

import sys
st.write(sys.executable)