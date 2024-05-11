import streamlit as st
import requests
import geopandas as gpd
import plotly.express as px
import pandas as pd

from DataBase_Countries import country_codes, get_country_code, get_country_name

# Function modified to fetch data and immediately calculate the visa-free rankings
def fetch_and_sort_visa_data(passport_code):
    """Fetch visa status data from the API and sort visa-free countries."""
    url = f'https://rough-sun-2523.fly.dev/api/{passport_code}'
    response = requests.get(url)
    data = response.json()
    return data
    
def plot_map(data):
    """Plotting the visa requirements map."""
    # Implementation for plotting, using data
    df = pd.DataFrame(data)
    fig = px.choropleth(df)
    st.plotly_chart(fig)

def run_visa_country_status():
    """Main function to run the Streamlit app."""
    st.title('Visa Country Status')
    
    selected_country = st.selectbox('Select your passport country:', list(country_codes.keys()), key='status_selected_country')
    passport_code = get_country_code(selected_country)

    if st.button('Show Visa Requirements Map'):
        data, ranking = fetch_and_sort_visa_data(passport_code)  # Fetch and sort data
        if data:
            plot_map(data)
            if ranking:
                st.write(f"Did you know that {selected_country} is number {ranking.index((selected_country, next(x[1] for x in ranking if x[0] == selected_country))) + 1} in visa-free states?")
            else:
                st.write("Ranking data for the selected country is not available.")
        else:
            st.error("No visa data available for the selected country.")

if __name__ == "__main__":
    run_visa_country_status()

            






