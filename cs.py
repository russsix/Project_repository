#cs.py
import streamlit as st
from two_states import run_visa_checker
from one_state_copy import run_visa_country_status


def run_flight_comparison():
    st.sidebar.write("Flight Comparison feature coming soon.")

st.sidebar.title('Navigation')
app_option = st.sidebar.selectbox('Choose a feature:',
    ('Two States', 'Visa Country Status', 'Flight Comparison'))

if app_option == 'Two States':
    run_visa_checker()
elif app_option == 'Visa Country Status':
    run_visa_country_status()
elif app_option == 'Flight Comparison':
    run_flight_comparison()
