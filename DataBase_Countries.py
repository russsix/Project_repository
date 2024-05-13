#DataBase_Countries

import pandas as pd

def load_country_codes(file_name):
    # Load the CSV file from the given filename
    df = pd.read_csv(file_name, header=None)  # Specify header=None to indicate no header in the CSV file
    
    # Create a dictionary with country names as keys and two-letter codes as values
    country_code_dict = pd.Series(df[1].values, index=df[0]).to_dict()
    
    return country_code_dict

file_name = 'country-code.csv'
country_codes = load_country_codes(file_name)

    
def get_country_code(country_name):
    return country_codes.get(country_name, None)

country_names = {code: country for country, code in country_codes.items()}
def get_country_name(code):
    return country_names.get(code, 'None')