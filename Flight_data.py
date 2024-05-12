import streamlit as st
import requests
import time

#Calls the flights/auto-complete API to get the information associated to a city
def city_id_search(city):
    url = "https://sky-scanner3.p.rapidapi.com/flights/auto-complete"
    querystring = {"query": city, "placeTypes": "CITY"}
    headers = {
        "X-RapidAPI-Key": "ffccb5b056msh29719849c313535p1a690fjsn51013f7ccb7c",
        "X-RapidAPI-Host": "sky-scanner3.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

#Extracts the id associated with the city from the flights/auto-complete response
def extract_city_id(response_data):
    city_info = []
    try:    
        for item in response_data['data']:
            suggestion_title = item['presentation']['suggestionTitle']
            presentation_id = item['presentation']['id']
            city_info.append({'suggestionTitle': suggestion_title, 'presentationId': presentation_id})
            
    except KeyError as e:
        print(f"KeyError: {e} - 'data' key not found in response_data")
        
    return city_info

#function to call API for one way trips
def get_one_way_flights(from_entity_id, to_entity_id, depart_date, market, locale, currency, adults, children, infants, cabin_class):
    url = "https://sky-scanner3.p.rapidapi.com/flights/search-one-way"
    querystring = {
        "fromEntityId": from_entity_id,
        "toEntityId": to_entity_id,
        "departDate": depart_date,
        "market": market,
        "locale": locale,
        "currency": currency,
        "adults": adults,
        "children": children,
        "infants": infants,
        "cabinClass": cabin_class
    }
    headers = {
        "X-RapidAPI-Key": "ffccb5b056msh29719849c313535p1a690fjsn51013f7ccb7c",
        "X-RapidAPI-Host": "sky-scanner3.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

#function to call API for round trips
def get_round_trip_flights(from_entity_id, to_entity_id, depart_date, return_date, market, locale, currency, adults, children, infants, cabin_class = 'economy'):
    url = "https://sky-scanner3.p.rapidapi.com/flights/search-roundtrip"
    querystring = {
        "fromEntityId": from_entity_id,
        "toEntityId": to_entity_id,
        "departDate": depart_date,
        "returnDate": return_date,
        "market": market,
        "locale": locale,
        "currency": currency,
        "adults": adults,
        "children": children,
        "infants": infants,
        "cabinClass": cabin_class
    }
    headers = {
        "X-RapidAPI-Key": "ffccb5b056msh29719849c313535p1a690fjsn51013f7ccb7c",
        "X-RapidAPI-Host": "sky-scanner3.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

# Function to check the status and fetch results if incomplete
def search_incomplete_fix(session_id):
    url = "https://sky-scanner3.p.rapidapi.com/flights/search-incomplete"
    headers = {
        "X-RapidAPI-Key": "ffccb5b056msh29719849c313535p1a690fjsn51013f7ccb7c",
        "X-RapidAPI-Host": "sky-scanner3.p.rapidapi.com"
    }
    querystring = {"sessionId": session_id}

    while True:
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()

        # Check if 'data' key exists and if 'context' and 'status' keys exist within 'data'
        if 'data' in data and 'context' in data['data'] and 'status' in data['data']['context']:
            status = data['data']['context']['status']
            if status == "incomplete":
                print("Searching for results...")
            elif status == "complete":
                print("Current status:", status)
                return data
            else:
                time.sleep(5)  # Wait for 10 seconds before making a new request
        else:
            print("Unexpected API response format:", data)
            break  # Exit loop if response format is not as expected

            
#extract from the full API response, the data that interests us           
def extract_flight_information(flight_search_results):
    flights = flight_search_results['data']['itineraries']
    flight_details = []
    
    for flight in flights:
        origin_info = flight['legs'][0]['origin']
        destination_info = flight['legs'][0]['destination']
        
        # Extract the 'name' from the origin dictionary if it exists and is well-formed
        origin_name = origin_info.get('name') if isinstance(origin_info, dict) and 'name' in origin_info else "Unknown origin"
        destination_name = destination_info.get('name') if isinstance(destination_info, dict) and 'name' in destination_info else "Unknown destination"
        
        details = {
            'priceRaw': flight['price']['raw'],
            'priceFormatted': flight['price']['formatted'],
            'origin': origin_name,
            'destination': destination_name,
            'durationInMinutes': flight['legs'][0]['durationInMinutes'],
            'stopCount': flight['legs'][0]['stopCount'],
            'departure': flight['legs'][0]['departure'],
            'arrival': flight['legs'][0]['arrival'],
            'carriersName': [carrier['name'] for carrier in flight['legs'][0]['carriers']['marketing']],
            'carriersLogo': [carrier['logoUrl'] for carrier in flight['legs'][0]['carriers']['marketing']],  
            'flightNumber': flight['legs'][0]['segments'][0]['flightNumber'],
        }
        flight_details.append(details)
                
    return flight_details

#function to sort results
def sort_flights(flight_details, sort_by, ascending=True, max_results=None):
    if sort_by == 'priceRaw':
        key_func = lambda x: x['priceRaw']
    elif sort_by == 'durationInMinutes':
        key_func = lambda x: x['durationInMinutes']
    elif sort_by == 'stopCount':
        key_func = lambda x: x['stopCount']
    else:
        return flight_details  # No sorting if sort_by criteria is unknown
    
    sorted_details = sorted(flight_details, key=key_func, reverse=not ascending)
    if max_results is not None:
        sorted_details = sorted_details[:max_results]
    return sorted_details


def display_flights(flight_details):
    for flight in flight_details:
        # Define the columns with relative widths
        cols = st.columns([3, 5, 1.5, 5, 2])

        with cols[0]:
            st.image(flight['carriersLogo'][0], width=80)  # Adjust width as needed
            st.text(flight['carriersName'][0])  # Carrier name below the logo

        with cols[1]:
            st.text("From:")
            st.text(flight['origin'])
            st.text("To:")
            st.text(flight['destination'])

        with cols[2]:
            st.text("Price:")
            st.text(flight['priceFormatted'].lstrip('$'))
            st.text(f"{currency}")
            
        with cols[3]:
            st.text("Departure:")
            st.text(flight['departure'])
            st.text("Arrival:")
            st.text(flight['arrival'])
            
        with cols[4]:
            st.text("Duration:")
            st.text(f"{flight['durationInMinutes']} min")
            st.text(f"Stops: {flight['stopCount']}")

        st.markdown("---")

    
st.title('Flight Search Tool')

# Define a mapping from user-friendly terms to data keys
sorting_options = {
    "Price": "priceRaw",
    "Duration": "durationInMinutes",
     "Number of Stops": "stopCount"
 }

 # Initialize session state variables if not already set
if 'flight_details' not in st.session_state:
    st.session_state.flight_details = []

with st.form("flight_form"):
    from_entity = st.text_input("Departure City", "New York")
    to_entity = st.text_input("Arrival City", "London")
    depart_date = st.date_input("Departure Date")
    currency = st.selectbox("Currency", ['CHF', 'EUR', 'USD'], index=1)
    adults = st.slider("Adults (12+)", 0, 8, 0)
    children = st.slider("Children (2-12)", 0, 8, 0)
    infants = st.slider("Infants (under 2)", 0, 8, 0)
    cabin_class = st.selectbox("Cabin Class", ['economy', 'premium_economy', 'business', 'first'])
    submit_button = st.form_submit_button("Search Flights")

if submit_button:
    # Check if no passengers are entered
    if adults == 0 and children == 0 and infants == 0:
        st.error("Please enter passengers.")
    else:
        dep_results = city_id_search(from_entity)
        arr_results = city_id_search(to_entity)
        if dep_results and arr_results:
            from_entity_id = extract_city_id(dep_results)[0]['presentationId']
            to_entity_id = extract_city_id(arr_results)[0]['presentationId']
            flights = get_one_way_flights(from_entity_id, to_entity_id, str(depart_date), 'US', 'en-US', currency, adults, children, infants, cabin_class)

            if 'data' in flights and 'context' in flights['data'] and 'status' in flights['data']['context']:
                if flights['data']['context']['status'] == "incomplete":
                    st.warning("Completing results...")
                    session_id = flights['data']['context']['sessionId']
                    flights = search_incomplete_fix(session_id)
                    st.success("Results completed.")
                else:
                    st.success("Results are complete.")

                st.session_state.flight_details = extract_flight_information(flights)

# Display sorting options and results count input outside the form to interact dynamically
sort_by = st.selectbox("Sort by", list(sorting_options.keys()), key="sort_by")
sort_order = st.radio("Sort order", ['Ascending', 'Descending'], key="sort_order")
result_count = st.number_input("Max results to display", 1, 100, 10, key="result_count")

if st.session_state.flight_details:
    sorted_flights = sort_flights(st.session_state.flight_details, sorting_options[sort_by], ascending=(sort_order == 'Ascending'), max_results=result_count)
    display_flights(sorted_flights)
else:
    st.error("Flight search did not return expected data or no search has been initiated.")

def flight_main():
    st.title('Flight Search Tool')

    with st.form("flight_form"):
        from_entity = st.text_input("Departure City", "New York")
        to_entity = st.text_input("Arrival City", "London")
        depart_date = st.date_input("Departure Date")
        currency = st.selectbox("Currency", ['CHF', 'EUR', 'USD'], index=1)
        adults = st.slider("Adults (12+)", 0, 8, 0)
        children = st.slider("Children (2-12)", 0, 8, 0)
        infants = st.slider("Infants (under 2)", 0, 8, 0)
        cabin_class = st.selectbox("Cabin Class", ['economy', 'premium_economy', 'business', 'first'])
        submit_button = st.form_submit_button("Search Flights")

    if submit_button:
        if adults == 0 and children == 0 and infants == 0:
            st.error("Please enter passengers.")
        else:
            dep_results = city_id_search(from_entity)
            arr_results = city_id_search(to_entity)
            if dep_results and arr_results:
                from_entity_id = extract_city_id(dep_results)[0]['presentationId']
                to_entity_id = extract_city_id(arr_results)[0]['presentationId']
                flights = get_one_way_flights(from_entity_id, to_entity_id, str(depart_date), 'US', 'en-US', currency, adults, children, infants, cabin_class)

                if 'data' in flights and 'context' in flights['data'] and 'status' in flights['data']['context']:
                    if flights['data']['context']['status'] == "incomplete":
                        st.warning("Completing results...")
                        session_id = flights['data']['context']['sessionId']
                        flights = search_incomplete_fix(session_id)
                        st.success("Results completed.")
                    else:
                        st.success("Results are complete.")

                    st.session_state.flight_details = extract_flight_information(flights)

                # Display sorting options and results count input outside the form to interact dynamically
                sort_by = st.selectbox("Sort by", list(sorting_options.keys()), key="sort_by")
                sort_order = st.radio("Sort order", ['Ascending', 'Descending'], key="sort_order")
                result_count = st.number_input("Max results to display", 1, 100, 10, key="result_count")

                if st.session_state.flight_details:
                    sorted_flights = sort_flights(st.session_state.flight_details, sorting_options[sort_by], ascending=(sort_order == 'Ascending'), max_results=result_count)
                    display_flights(sorted_flights)
                else:
                    st.error("Flight search did not return expected data or no search has been initiated.")

# Calling main() when the script is run (if not imported)
if __name__ == '__main__':
    flight_main()