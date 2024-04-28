import streamlit as st
import geopandas as gpd
import matplotlib.pyplot as plt
from DataBase_Countries import get_country_code, get_country_name

def get_country_color(country_code, visa_data):
    if country_code in visa_data:
        visa_status = visa_data[country_code]
        if visa_status == 'vf':
            return 'green'  # Visa Free
        elif visa_status == 'voa':
            return 'orange'  # Visa on Arrival
        elif visa_status == 'vr':
            return 'red'  # Visa Required
    return 'gray'  # No data

def plot_map(visa_data):
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    world['color'] = world['iso_a3'].apply(lambda x: get_country_color(x, visa_data))

    fig, ax = plt.subplots(figsize=(15, 10))
    world.plot(ax=ax, color=world['color'])
    ax.set_title('Visa Requirements Map')
    ax.set_axis_off()
    st.pyplot(fig)

def run_visa_country_status():
    st.title('Visa Country Status')
    passport_country = st.text_input("Enter your departure country:", key='departure_country')
    passport_code = get_country_code(passport_country) if passport_country else None
    
    if passport_country and not passport_code:
        st.error(f"'{passport_country}' is not recognized. Please enter a valid country name.")

    if st.button('Visa Country Status') and passport_code:
        url = f'https://rough-sun-2523.fly.dev/api/{passport_code}'
        response = requests.get(url)
        data = response.json()
        if data:
            visa_data = {}
            visa_required_countries = data.get('vr', {}).get('data', [])
            visa_on_arrival_countries = data.get('voa', {}).get('data', [])
            visa_free_countries = data.get('vf', {}).get('data', [])
            for country_code in visa_required_countries:
                visa_data[country_code] = 'vr'
            for country_code in visa_on_arrival_countries:
                visa_data[country_code] = 'voa'
            for country_code in visa_free_countries:
                visa_data[country_code] = 'vf'

plot_map(visa_data)

run_visa_country_status()
