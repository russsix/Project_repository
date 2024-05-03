#DataBase_Countries

import pandas as pd

def load_country_codes(file_name):
    # Load the CSV file from the given filename
    df = pd.read_csv(file_name, header=None)  # Specify header=None to indicate no header in the CSV file
    
    # Assume the columns are in the same order as 'Country' and 'Country_Code_2'
    # Create a dictionary with country names as keys and two-letter codes as values
    country_code_dict = pd.Series(df[1].values, index=df[0]).to_dict()
    
    return country_code_dict

file_name = 'country-code.csv'
country_codes = load_country_codes(file_name)

    
normalized_country_codes = {key: value for key, value in country_codes.items()}
def get_country_code(country_name):
    normalized_name = country_name.strip().lower()
    return normalized_country_codes.get(normalized_name, None)

country_names = {code: country for country, code in country_codes.items()}
def get_country_name(code):
    normalized_code = code.strip().lower()
    return country_names.get(normalized_code, 'None')