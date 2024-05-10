import requests 

def fetch_visa_status_data(passport_code):
    """Fetch visa status data from the API."""
    url = f'https://rough-sun-2523.fly.dev/api/{passport_code}'
    response = requests.get(url)
    data = response.json()
    return data


def get_visa_free_count(passport_code):
    data = fetch_visa_status_data(passport_code)
    visa_free_countries = [country for country, status in data.items() if status == "visa-free"]
    return len(visa_free_countries)


def get_ranked_countries():
    """Get a list of countries ranked by the number of visa-free countries."""
    country_ranks = []

    for country, code in country_codes.items():
        visa_free_count = get_visa_free_count(code)
        country_ranks.append((country, visa_free_count))

    # Sort by visa-free count descending
    ranked_countries = sorted(country_ranks, key=lambda x: x[1], reverse=True)
    return ranked_countries

# Execute the ranking function
rank_countries()
