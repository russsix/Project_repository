import streamlit as st
import pydeck as pdk
import geopandas as gpd
import pandas as pd

def set_country_colors(geo_dataframe, country_column, color_map):
    """
    Adds a 'color' column to the GeoDataFrame based on the country name.

    Parameters:
    - geo_dataframe: A GeoDataFrame containing the geographical data.
    - country_column: The name of the column in the GeoDataFrame that contains country names.
    - color_map: A dictionary mapping country names to color values.

    Returns:
    - A GeoDataFrame with a new 'color' column.
    """
    # Initialize a 'color' column with default colors
    geo_dataframe['color'] = [color_map.get('default')] * len(geo_dataframe)

    for country, color in color_map.items():
        geo_dataframe.loc[geo_dataframe[country_column] == country, 'color'] = color

    return geo_dataframe

# Example usage:

# Load your geographical data into a GeoDataFrame
geo_df = gpd.read_file(r"D:\Download\global_states.geojson")

# Define a color map for countries
color_map = {
    'United States of America': [255, 0, 0, 160],  # Red for the US
    'default': [34, 139, 34, 160]  # Green for other countries
}

# Apply the color settings to the GeoDataFrame
geo_df = set_country_colors(geo_df, 'ADMIN', color_map)

# Convert the GeoDataFrame to a format that Pydeck understands
geojson = geo_df.__geo_interface__

# Create the Pydeck layer with custom colors
layer = pdk.Layer(
    "GeoJsonLayer",
    geojson,
    get_fill_color='properties.color',
    pickable=True,
    auto_highlight=True
)

# Set the initial view state
view_state = pdk.ViewState(latitude=0, longitude=0, zoom=1)

# Create and display the Pydeck chart
r = pdk.Deck(layers=[layer], initial_view_state=view_state, map_style='mapbox://styles/mapbox/light-v9')
st.pydeck_chart(r)
