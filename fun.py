import streamlit as st
import requests
import geopandas as gpd
import plotly.express as px
import sys
import pandas as pd
from one_state import run_visa_country_status

from DataBase_Countries import country_codes, get_country_code, get_country_name

def get_visa_rank()
visa_free_countries = [get_country_name(code) for code in visa_data.get('vf', {}).get('data', [])]
if visa_free_countries:
    rank = visa_free_countries.index(selected_country) + 1
    st.write(f"Did you know that {selected_country} is number {rank} with visa free states.")

