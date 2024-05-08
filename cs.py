#cs.py
import streamlit as st
import sys
sys.path.append('rachelemantero/Project_repository')
from two_states import run_visa_checker
from one_state import run_visa_country_status
from fun import get_visa_rank


def run_flight_comparison():
    st.sidebar.write("Flight Comparison feature coming soon.")
def main():
    st.sidebar.title('Navigation')
    app_option = st.sidebar.selectbox('Choose a feature:',
        ('Two States', 'Visa Country Status', 'Flight Comparison'))

    if app_option == 'Two States':
        run_visa_checker()
    elif app_option == 'Visa Country Status':
        run_visa_country_status()
    elif app_option == 'Flight Comparison':
        run_flight_comparison()

if __name__ == "__main__":
    main()
