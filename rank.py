import requests 

def fetch_visa_status_data(passport_code):
    """Fetch visa status data from the API."""
    url = f'https://rough-sun-2523.fly.dev/api/{passport_code}'
    response = requests.get(url)
    data = response.json()
    return data
    

def count_visa_free_states(visa_data):
    result = [(country, sum(1 for visa_status in destinations.values() if visa_status == 'visa-free'))
        for country, destinations in visa_data.items() ]
    # Sort the result by the count of visa-free countries in descending order
    sorted_result = sorted(result, key=lambda x: x[1], reverse=True)
    return sorted_result
