import streamlit as st
from two_states import run_visa_checker

# Placeholder functions for the other features
def run_visa_free_destinations():
    st.write("Visa-Free Destinations feature coming soon.")

def run_flight_comparison():
    st.write("Flight Comparison feature coming soon.")

st.markdown("""
<style>
    .background {
        position: absolute;
        width: 100%;
        height: 100%;
        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;
        background-image: url("https://img.freepik.com/free-photo/painting-mountain-lake-with-mountain-background_188544-9126.jpg");
        z-index: -1;
        top: 0;
        left: 0;
    }

    h1 {
        color: white;
        text-align: center;
    }

    .feature-card {
        background: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        padding: 10px;
        margin: 10px;
    }

    /* Additional styles to enhance the feature card appearance */
    .stButton>button {
        font-size: 16px;
        width: 100%;
        border-radius: 10px;
        border: 2px solid #f63366;
        margin: 10px 0;
    }
</style>
<div class="background"></div>
""", unsafe_allow_html=True)

# Display the app title
st.title('🌍 Check-it')

# Create the layout with columns and feature cards
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🌍 Two States", key="two_states"):
        run_visa_checker()

with col2:
    if st.button("✈️ Visa-Free Destinations", key="visa_free_destinations"):
        run_visa_free_destinations()

with col3:
    if st.button("🧳 Flight Comparison", key="flight_comparison"):
        run_flight_comparison()
