import streamlit as st
import sys
sys.path.append('rachelemantero/Project_repository')
from two_states import run_visa_checker
from one_state import run_visa_country_status

def main():
    # Set the page title
    st.set_page_config(page_title="Check-It")

    # Large sidebar title using HTML for styling
    st.sidebar.markdown("<h1 style='font-size: 32px; color: black; margin-top: 0;'>Check-It ✅</h1>", unsafe_allow_html=True)

    # Sidebar navigation and welcome text
    st.sidebar.write("Welcome to the Visa and Travel Assistant! Select a feature from the list below to get started.")
    app_option = st.sidebar.selectbox('Choose a feature:',
                                      ['Two States', 'Visa Country Status', 'Flight Comparison'])

    # Smaller main page title using HTML for top-left styling
    st.markdown("<h2 style='font-size: 18px; color: black; position: absolute; top: 0; right: 0;'>Check-It ✅</h2>", unsafe_allow_html=True)
    
    # Conditional execution based on sidebar selection
    if app_option == 'Two States':
        run_visa_checker()
    elif app_option == 'Visa Country Status':
        run_visa_country_status()

if __name__ == "__main__":
    main()
