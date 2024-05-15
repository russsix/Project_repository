#DataBase_Countries
"""This files takes informations from the country-code.csv, that was found in the API documentation,
and creates a dictionary with the corresponding keys and values"""

import pandas as pd

def load_country_codes(file_name):
    # Load the CSV file from the given filename
    df = pd.read_csv(file_name, header=None)  
    
    # Create a dictionary with country names as keys and two-letter codes as values
    country_code_dict = pd.Series(df[1].values, index=df[0]).to_dict()
    
    return country_code_dict

file_name = 'country-code.csv'
country_codes = load_country_codes(file_name)

# Gets country codes for given country names    
def get_country_code(country_name):
    return country_codes.get(country_name, None)

country_names = {code: country for country, code in country_codes.items()} # Creates a dictionary switching country codes and names as keys and values

# Gets country names for given country codes
def get_country_name(code):
    return country_names.get(code, 'None')