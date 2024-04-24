import streamlit as st
import folium
import requests
from DataBase_Countries import get_country_code, get_country_name

def run_visa_checker():
    st.title('Visa Country Status')
    departure_country = st.text_input("Enter your departure country:", key='departure_country')
    departure_code = get_country_code(departure_country) if departure_country else None
    
    if departure_country and not departure_code:
        st.error(f"'{departure_country}' is not recognized. Please enter a valid country name.")

    if st.button('Visa Country Status') and departure_code:
        url = f'https://rough-sun-2523.fly.dev/api/{departure_code}'
        response = requests.get(url)
        if response.status_code == 200:
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
        else:
            st.error(f"Failed to retrieve data. Status code: {response.status_code}")

run_visa_checker()

# Create a base map
m = folium.Map(location=[0, 0], zoom_start=2)

# Function to determine color based on whether the country is selected or not
def get_color(country):
    if country in st:
        return 'green'
    else:
        return 'red'

# Add countries to the map
for country in ['USA', 'Canada', 'Mexico', 'France', 'Germany', 'Japan']:
    folium.CircleMarker(
        location=[0, 0],
        radius=5,
        color=get_color(country),
        fill=True,
        fill_color=get_color(country),
        fill_opacity=0.7,
        tooltip=country
    ).add_to(m)

# Display the map
st.markdown(m._repr_html_(), unsafe_allow_html=True)
