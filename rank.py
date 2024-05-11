import requests 
from DataBase_Countries import country_codes

def fetch_visa_status_data(passport_code):
    """Fetch visa status data from the API."""
    url = f'https://rough-sun-2523.fly.dev/api/{passport_code}'
    response = requests.get(url)
    data = response.json()
    return data
    
visa_free_counts = {}
for country, code in country_codes.items():
    visa_free = [get_country_name(code) for code in data.get('vf', {}).get('data', [])]
    visa_free_counts[country] = len(visa_free)
sorted_visa_free = sorted(visa_free_counts.items(), key=lambda x: x[1], reverse=True)

