import streamlit as st
import sys
sys.path.append('rachelemantero/Project_repository')
from two_states import run_visa_checker
from one_state import run_visa_country_status

def main():
    # Set the page title without a favicon
    st.set_page_config(page_title="Check-It")

    # Using HTML to style the sidebar title as smaller and aligned at the top-left
    st.sidebar.markdown("<h1 style='font-size: 18px; color: black; margin-top: 0;'>Check-It ✅</h1>", unsafe_allow_html=True)

    # Sidebar navigation and welcome text
    st.sidebar.write("Welcome to the Visa and Travel Assistant! Select a feature from the list below to get started.")
    app_option = st.sidebar.selectbox('Choose a feature:',
                                      ['Two States', 'Visa Country Status', 'Flight Comparison'])

    # Execute appropriate function based on user choice
    if app_option == 'Two States':
        run_visa_checker()
    elif app_option == 'Visa Country Status':
        run_visa_country_status()

if __name__ == "__main__":
    main()
