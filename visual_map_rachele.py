import streamlit as st
import pydeck as pdk

# Define the GeoJsonLayer
layer = pdk.Layer(
    'GeoJsonLayer',
    'D:/Download/global_states.geojson',
    get_fill_color='[200, 30, 0, 160]',  # Set the fill color to a semi-transparent red
    get_line_color='[255, 255, 255, 255]',  # Set the line color to white for the boundaries
    pickable=True,
    auto_highlight=True,
)

# Define the initial view state with a wider longitude span
view_state = pdk.ViewState(
    longitude=0,
    latitude=0,
    zoom=1.1,  # The zoom level that shows the entire map might need some trial and error
)

# Create the Deck.gl map
r = pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    map_style=pdk.map_styles.LIGHT,  # A light map style
    width='100%',  # Width of the map
    height=500,  # Height of the map in pixels
)

st.pydeck_chart(r)
