import streamlit as st
import requests
import folium

def get_visa_free_destinations(passport_country):
    api_url = f'https://rough-sun-2523.fly.dev/api/{passport_country}'
    response = requests.get(api_url)
    return response.json()
        
def main():
    st.title("Visa-Free Travel Destinations")
    passport_country = st.text_input("Enter your passport country: ")
    if st.button("Search"):
        visa_free_destinations = get_visa_free_destinations(passport_country)
        if visa_free_destinations:
            st.write(f"Visa-Free travel destinations for {passport_country}:")
            for destination_country in visa_free_destinations:
                st.write(destination_country)
        else:
            st.write("No visa-free travel destinations found.")
        
        # Create a base map
        m = folium.Map(location=[0, 0], zoom_start=2)

        # Function to determine color based on whether the country is selected or not
        def get_color(country):
            if country in visa_free_destinations:
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

if __name__ == "__main__":
    main()


