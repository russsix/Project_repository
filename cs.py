# cs.py
from two_states import run_visa_checker
st.title('Check-it')
app_mode = st.sidebar.radio(
    "Choose the feature you want to use:",
    ("Visa Requirement Checker", "Visa-Free Destinations", "Flight Suggestions")
)
if app_mode == "Visa Requirement Checker":
    run_visa_checker()
else:
    None




