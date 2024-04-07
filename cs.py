import streamlit as st
from two_states import run_visa_checker

# Custom CSS to set the background and style elements
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


# Create columns for different sections
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🛂 Visa Requirement Checker"):
        app_mode = "🛂 Visa Requirement Checker"

with col2:
    if st.button("✈️ Visa-Free Destinations"):
        app_mode = "✈️ Visa-Free Destinations"

with col3:
    if st.button("🧳 Flight Suggestions"):
        app_mode = "🧳 Flight Suggestions"

# Based on the selection, run the corresponding feature function
if app_mode == "🛂 Visa Requirement Checker":
    run_visa_checker()
elif app_mode == "✈️ Visa-Free Destinations":
    st.info("The Visa-Free Destinations feature is coming soon.")
elif app_mode == "🧳 Flight Suggestions":
    st.info("The Flight Suggestions feature is coming soon.")


"""fonti
https://docs.kanaries.net/topics/Streamlit/streamlit-theming"""