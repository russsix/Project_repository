#one_state_copy
import streamlit as st
import requests
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

    #insert passport country and get country code
    passport_country = st.text_input("Enter your departure country:", key='departure_country')
    passport_code = get_country_code(passport_country) if passport_country else None
    
    #does the passport country exist?
    if passport_country and not passport_code:
        st.error(f"'{passport_country}' is not recognized. Please enter a valid country name.")

    #print all the Visa required countries, the visa on arrival countries, the visa-free countries, the covid-ban countries and the no admission countries
    if st.button('Visa Country Status') and passport_code:
        url = f'https://rough-sun-2523.fly.dev/api/{passport_code}'
        response = requests.get(url)
        data = response.json()
        if data:
            # Visa Required Countries
            st.write("Visa Required Countries:")
            visa_required_countries = [get_country_name(code) for code in data.get('vr', {}).get('data', [])]
            st.write(', '.join(visa_required_countries))

            # Visa on Arrival Countries
            st.write("Visa on Arrival Countries:")
            visa_on_arrival_countries = [get_country_name(code) for code in data.get('voa', {}).get('data', [])]
            st.write(', '.join(visa_on_arrival_countries))

            # Visa Free Countries
            st.write("Visa Free Countries:")
            visa_free_countries = [get_country_name(code) for code in data.get('vf', {}).get('data', [])]
            st.write(', '.join(visa_free_countries))

            # Covid Ban Countries
            if data.get('cb', {}).get('data'):
                st.write("Covid Ban Countries:")
                covid_ban_countries = [get_country_name(code) for code in data.get('cb', {}).get('data', [])]
                st.write(', '.join(covid_ban_countries))

            # No Admission Countries
            if data.get('na', {}).get('data'):
                st.write("No Admission Countries:")
                no_admission_countries = [get_country_name(code) for code in data.get('na', {}).get('data', [])]
                st.write(', '.join(no_admission_countries))
        

run_visa_country_status()
