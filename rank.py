import requests 
from DataBase_Countries import country_codes

def fetch_visa_status_data(passport_code):
    """Fetch visa status data from the API."""
    url = f'https://rough-sun-2523.fly.dev/api/{passport_code}'
    response = requests.get(url)
    data = response.json()
    return data
    
#takes the dictionary 
def count_visa_free_countries(country_codes):
    #empty dictionary to store visa count
    visa_free_counts = {}
    for country, code in country_codes.items():
        visa_free = fetch_visa_free_countries(code)
        visa_free_counts[country] = len(visa_free)
    sorted_visa_free = sorted(visa_free_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_visa_free

