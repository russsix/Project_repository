import streamlit as st
from two_states import run_visa_checker


def set_background_image():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://your-image-url.com/your-image.jpg");
            background-size: cover;
            background-position: center center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the function to set the background image
set_background_image()

st.title('Check-it')

app_mode = st.sidebar.radio(
    "Choose the feature you want to use:",
    ("🛂 Visa Requirement Checker", "✈️ Visa-Free Destinations", "🧳 Flight Suggestions")
)

if app_mode == "🛂 Visa Requirement Checker":
    run_visa_checker()
elif app_mode == "✈️ Visa-Free Destinations":
    st.info("The Visa-Free Destinations feature is coming soon.")
elif app_mode == "🧳 Flight Suggestions":
    st.info("The Flight Suggestions feature is coming soon.")
