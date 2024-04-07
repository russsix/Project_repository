import streamlit as st
from two_states import run_visa_checker

# Assume these functions exist in separate modules that you've created for each feature.
# from visa_free import run_visa_free
# from flight_comparison import run_flight_comparison

# Define a function for each feature that you want to run when its corresponding button is clicked
def run_visa_free():
    st.write("Visa-Free Destinations feature will be implemented here.")

def run_flight_comparison():
    st.write("Flight Comparison feature will be implemented here.")

# Use session state to keep track of which feature is active
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = None

# Layout with feature cards
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🌍 Two States"):
        st.session_state['current_page'] = 'visa_checker'

with col2:
    if st.button("✈️ Three States"):
        st.session_state['current_page'] = 'visa_free'

with col3:
    if st.button("🧳 Flight Comparison"):
        st.session_state['current_page'] = 'flight_comparison'

# Logic to handle page navigation
if st.session_state['current_page'] == 'visa_checker':
    run_visa_checker()
elif st.session_state['current_page'] == 'visa_free':
    run_visa_free()
elif st.session_state['current_page'] == 'flight_comparison':
    run_flight_comparison()
