import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from DataBase_Countries import get_country_code, get_country_name
from one_state_copy import run_visa_country_status

run_visa_country_status()

# Create a list of countries

countries = ['vr': {'data': ['AF', 'DZ', 'CF', 'TD', 'CG', 'ER', 'GH', 'LR', 'ML', 'NR', 'NE', 'KP', 'SD', 'SY', 'TM', 'YE'], 'length': 16}, 'voa': {'data': ['AU', 'BH', 'BD', 'BF', 'BI', 'KH', 'CA', 'KM', 'CI', 'CU', 'DJ', 'EG', 'ET', 'GW', 'ID', 'IR', 'IQ', 'JO', 'KE', 'KW', 'LB', 'MG', 'MW', 'MV', 'MH', 'MR', 'NP', 'NZ', 'OM', 'PK', 'PW', 'PG', 'QA', 'WS', 'SA', 'SC', 'SL', 'SO', 'LK', 'SR', 'TZ', 'TG', 'US', 'ZM', 'ZW'], 'length': 45}, 'vf': {'data': ['AL', 'AD', 'AO', 'AG', 'AR', 'AM', 'AT', 'AZ', 'BS', 'BB', 'BY', 'BE', 'BZ', 'BJ', 'BT', 'BO', 'BA', 'BW', 'BR', 'BN', 'BG', 'CM', 'CV', 'CL', 'CN', 'CO', 'CD', 'CR', 'HR', 'CY', 'CZ', 'DK', 'DM', 'DO', 'EC', 'SV', 'GQ', 'EE', 'SZ', 'FJ', 'FI', 'FR', 'GA', 'GM', 'GE', 'DE', 'GR', 'GD', 'GT', 'GN', 'GY', 'HT', 'HN', 'HK', 'HU', 'IS', 'IN', 'IE', 'IL', 'IT', 'JM', 'JP', 'KZ', 'KI', 'XK', 'KG', 'LA', 'LV', 'LS', 'LY', 'LI', 'LT', 'LU', 'MO', 'MY', 'MT', 'MU', 'MX', 'FM', 'MD', 'MC', 'MN', 'ME', 'MA', 'MZ', 'MM', 'NA', 'NL', 'NI', 'NG', 'MK', 'NO', 'PS', 'PA', 'PY', 'PE', 'PH', 'PL', 'PT', 'RO', 'RU', 'RW', 'KN', 'LC', 'SM', 'ST', 'SN', 'RS', 'SG', 'SK', 'SI', 'SB', 'ZA', 'KR', 'SS', 'ES', 'VC', 'SE', 'TW', 'TJ', 'TH', 'TL', 'TO', 'TT', 'TN', 'TV', 'TR', 'UG', 'UA', 'AE', 'GB', 'UY', 'UZ', 'VU', 'VA', 'VE', 'VN']  # Example list of countries

# Create a list to store visa requirements for each country (0 - No visa required, 1 - Visa required, 2 - Visa on arrival)
visa_requirements = [0, 1, 2]  

# Create a colormap for visa requirements
colors = ['green' if visa == 0 else 'red' if visa == 1 else 'orange' for visa in visa_requirements]
cmap = ListedColormap(colors)

# Plot countries and colors using Matplotlib
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title('Countries Visa Requirements')
ax.barh(countries, visa_requirements, color=colors)
ax.set_xlabel('Visa Requirement')
ax.set_ylabel('Country')

# Display Matplotlib plot in Streamlit
st.pyplot(fig)

