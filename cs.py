# cs.py
from two_states import run_visa_checker

# Run the visa checker feature imported from two_states.py
run_visa_checker()


# Custom CSS
st.markdown("""
<style>
.custom-style {
    background-color: #262730;
    color: #21a1f1;
    padding: 10px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# Using the custom style in a container
with st.container():
    st.markdown('<div class="custom-style">This is a custom-styled container</div>', unsafe_allow_html=True)