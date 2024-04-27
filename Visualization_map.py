import streamlit as st
import pydeck as pdk
import geopandas as gpd

# Load geographical data from the GeoJSON file
geo_data = gpd.read_file(r"D:\Download\global_states.geojson")

# Define a function to apply color based on the country
def color_countries(features):
    if features['properties']['ADMIN'] == 'United States of America':
        # Color the United States in red
        return [255, 0, 0]
    else:
        # Use a neutral color for other countries
        return [128, 128, 128]

# Use GeoPandas to iterate over the GeoDataFrame and apply colors
geo_data['color'] = geo_data.apply(lambda row: color_countries(row['geometry']), axis=1)

# Convert GeoDataFrame to JSON
geojson = geo_data.__geo_interface__

# Create the Pydeck layer
layer = pdk.Layer(
    "GeoJsonLayer",
    geojson,
    opacity=0.7,
    stroked=False,
    filled=True,
    get_fill_color='color',
)

# Set the initial view state
view_state = pdk.ViewState(
    latitude=0,
    longitude=0,
    zoom=1
)

# Render the Pydeck map with the custom layer
st.pydeck_chart(pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    # Use a map style that includes country labels
    map_style='mapbox://styles/mapbox/light-v10'
))
