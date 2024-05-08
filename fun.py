import streamlit as st
import requests
import geopandas as gpd
import plotly.express as px
import sys
import pandas as pd
from one_state import run_visa_country_status

from DataBase_Countries import country_codes, get_country_code, get_country_name

def get_visa_rank(
