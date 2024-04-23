import streamlit as st
from two_states import run_visa_checker

def run_visa_free_destinations():
    st.sidebar.write("Visa-Free Destinations feature coming soon.")

def run_flight_comparison():
    st.sidebar.write("Flight Comparison feature coming soon.")

st.sidebar.title('Navigation')
app_option = st.sidebar.selectbox('Choose a feature:',
    ('Two States', 'Visa-Free Destinations', 'Flight Comparison'))

if app_option == 'Two States':
    run_visa_checker()
elif app_option == 'Visa-Free Destinations':
    run_visa_free_destinations()
elif app_option == 'Flight Comparison':
    run_flight_comparison()
