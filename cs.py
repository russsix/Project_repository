import streamlit as st
import sys
sys.path.append('rachelemantero/Project_repository')
from two_states import run_visa_checker
from one_state import run_visa_country_status

def main():
    # Setting the title of the sidebar
    st.sidebar.title('Navigation')

    # Adding a general description of the app's functionality
    st.sidebar.write("Welcome to the Visa and Travel Assistant! Select a feature from the list below to get started.")

    # Feature selection with descriptions for each option
    app_option = st.sidebar.selectbox('Choose a feature:',
                                      options=[
                                          'Two States',
                                          'Visa Country Status',
                                          'Flight Comparison'
                                      ],
                                      format_func=lambda x: {'Two States': 'Two States - Compare visa requirements between two countries',
                                                             'Visa Country Status': 'Visa Country Status - Check visa requirements for a single country',
                                                             'Flight Comparison': 'Flight Comparison - Compare flight options and prices'}[x])

    # Executing the appropriate function based on user choice
    if app_option == 'Two States':
        run_visa_checker()
    elif app_option == 'Visa Country Status':
        run_visa_country_status()

if __name__ == "__main__":
    main()
