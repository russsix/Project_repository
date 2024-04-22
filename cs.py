import streamlit as st
from two_states import run_visa_checker

def run_visa_free_destinations():
    st.write("Visa-Free Destinations feature coming soon.")

def run_flight_comparison():
    st.write("Flight Comparison feature coming soon.")

# Set page config
st.set_page_config(page_title="Check-it", layout="wide", page_icon="🌍")

# Custom styles
st.markdown("""
<style>
    .streamlit-container {
        max-width: 1200px;
        margin: auto;
    }
    .stButton>button {
        width: 100%;
        border: none;
        padding: 1rem;
        font-size: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
        transition: background-color 0.3s, transform 0.3s;
    }
    .stButton>button:hover {
        background-color: #f63366;
        color: white;
        transform: translateY(-3px);
    }
    .stTextInput>div>div>input {
        padding: 0.75rem;
        border-radius: 0.5rem;
    }
    h1 {
        color: white;
    }
    .tab-style {
        box-shadow: none;
        border: 1px solid #fff;
        border-radius: 0.5rem;
        margin: 1rem 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Header section with a background image
st.markdown("""
<div style="background-color:#464e5f;padding:2rem;text-align:center;">
    <h1 style="color:white;font-size:3rem;">🌍 Check-it</h1>
</div>
""", unsafe_allow_html=True)

# Create the layout with tabs for a cleaner navigation experience
tab1, tab2, tab3 = st.tabs(["🌍 Two States", "✈️ Visa-Free Destinations", "🧳 Flight Comparison"])

with tab1:
    st.markdown("<div class='tab-style'>", unsafe_allow_html=True)
    run_visa_checker()
    st.markdown("</div>", unsafe_allow_html=True)

with tab2:
    st.markdown("<div class='tab-style'>", unsafe_allow_html=True)
    run_visa_free_destinations()
    st.markdown("</div>", unsafe_allow_html=True)

with tab3:
    st.markdown("<div class='tab-style'>", unsafe_allow_html=True)
    run_flight_comparison()
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("Check-it | A tool for all your travel documentation needs.")

# To apply styles globally across the app, including the sidebar
st.markdown("""
<style>
    /* This is to style the entire app with a background image, adjust the url accordingly */
    body {
        background-image: url("https://img.freepik.com/free-photo/painting-mountain-lake-with-mountain-background_188544-9126.jpg");
        background-size: cover;
        background-attachment: fixed;
    }
    /* This sets the sidebar style */
    .css-1d391kg {
        background-color: #f1f1f1;
        color: #666;
    }
    /* Customize the color of the active tab */
    .st-ae {
        background-color: #f63366;
        color: white;
    }
</style>
""", unsafe_allow_html=True)
