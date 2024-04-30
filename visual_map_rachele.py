import streamlit as st
import requests
import geopandas as gpd
import matplotlib.pyplot as plt
from DataBase_Countries import country_codes, get_country_code

def get_country_code(country_name):
    return country_codes.get(country_name.strip().title(), None)

def fetch_visa_status_data(passport_code):
    url = f'https://rough-sun-2523.fly.dev/api/{passport_code}'
    response = requests.get(url)
    return response.json() if response.ok else None

def visa_map():
    st.title('World Map by Visa Requirement Status')

    # User selects a country from a dropdown populated with available countries
    selected_country = st.selectbox('Select your passport country:', list(country_codes.keys()))

    if st.button('Show Visa Requirements Map'):
        passport_code = get_country_code(selected_country)
        if passport_code:
            visa_data = fetch_visa_status_data(passport_code)
            if visa_data:
                # Load geographical data from the GeoJSON file
                geo_df = gpd.read_file("D:\\Download\\global_states.geojson")

                # Prepare lists of countries based on visa requirement
                visa_required_countries = [c for c in visa_data.get('vr', {}).get('data', [])]
                visa_on_arrival_countries = [c for c in visa_data.get('voa', {}).get('data', [])]
                visa_free_countries = [c for c in visa_data.get('vf', {}).get('data', [])]

                # Define a function to return the color based on the visa status
                def color_for_visa_status(country):
                    if country in visa_required_countries:
                        return 'red'
                    elif country in visa_on_arrival_countries:
                        return 'yellow'
                    elif country in visa_free_countries:
                        return 'green'
                    else:
                        return 'grey'  # Default color if status is unknown

                # Apply the color to each country using the function
                geo_df['color'] = geo_df['ADMIN'].apply(color_for_visa_status)

                # Plot the GeoDataFrame
                fig, ax = plt.subplots(1, 1, figsize=(15, 10))
                geo_df.plot(ax=ax, color=geo_df['color'])

                # Remove axis for a cleaner look
                ax.axis('off')

                # Set a title for the map
                ax.set_title('World Map by Visa Requirement Status')

                # Show the plot using Streamlit
                st.pyplot(fig)
            else:
                st.error("Failed to retrieve visa data. Please try again.")
        else:
            st.error("Invalid country selected. Please choose a valid country from the list.")

visa_map()
