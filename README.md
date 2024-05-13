This is the description of the Group 1.4.

Our site has three different features.
The first is 'Two States'.
    The main goal is that the user inputs two countries and gets the Visa requirements between them.
The second is 'One State'.
    The main goal is that the user inputs his passport country and gets a world map color-coded with the Visa requirements for all the countries in the world.
The third is 'Flight Search'
    The main goal is that the user inputs their departure, destination country and other filters in order to get different flights ordered by price, duration and stops.

These three features are imported together in one main file 'cs.py'. In order to visualize the code on streamlit, you need to run this file.

Additional information
    For this code, we used two APIs, one for the visa requirements and one for the flight search.
    The file 'country_code.csv' is an excel retrieved from the documentation of the API and it contains all the inputs (countries) an user can ask the API.
    The file 'DataBase_Countries' reads the csv file and creates two dictionaries containing country names and codes. 
    The file 'global_states.geojson' contains a geojson file used in order to create a world map for the One State feature.