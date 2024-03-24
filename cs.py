import streamlit as st

st.write('yah')
from feature_01 import return_even
list_1= [i for i in range(10)]
even_list=return_even(list_1)
st.write (even_list)
