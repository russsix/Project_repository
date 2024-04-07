import streamlit as st
from two_states import run_visa_checker

# Custom CSS to inject into Streamlit
custom_css = """
<style>
    .reportview-container .main .block-container {
        padding-top: 5rem;
        padding-bottom: 5rem;
    }
    .reportview-container .main {
        background-image: url('https://www.synergytravelsindia.com/wp-content/uploads/2020/08/schengen-travel-visa.jpg');
        background-size: cover;
    }
    h1 {
        color: #f63366;
    }
    .sidebar .sidebar-content {
        background-color: #f1f1f1;
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

st.title('🌍 Check-it')

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
