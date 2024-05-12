#cs.py
import streamlit as st
import sys
sys.path.append('rachelemantero/Project_repository')
from two_states import run_visa_checker
from one_state import run_visa_country_status



def main():
    st.title("Check-It ✅")
    
    # Sidebar title
    st.sidebar.title('Navigation')
    st.sidebar.write("Welcome to the Visa and Travel Assistant! Select a feature from the list below to get started.")
    app_option = st.sidebar.selectbox('Choose a feature:',
        ('Two States', 'Visa Country Status', 'Flight Comparison'))

    if app_option == 'Two States':
        run_visa_checker()
    elif app_option == 'Visa Country Status':
        run_visa_country_status()

        

if __name__ == "__main__":
    main()
