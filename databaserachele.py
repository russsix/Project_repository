import pandas as pd
import streamlit as st
def load_country_codes(file_name):
    # Load the CSV file from the given filename
    df = pd.read_csv(file_name, header=None)  # Specify header=None to indicate no header in the CSV file
    
    # Assume the columns are in the same order as 'Country' and 'Country_Code_2'
    # Create a dictionary with country names as keys and two-letter codes as values
    country_code_dict = pd.Series(df[1].values, index=df[0]).to_dict()
    
    return country_code_dict

if __name__ == "__main__":
    # Since the CSV file is in the same directory, you can simply specify its name
    file_name = 'country-code.csv'
    country_codes = load_country_codes(file_name)
    print(country_codes)
st.write (country_codes)