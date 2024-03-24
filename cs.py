import streamlit as st
from feature_01.py import return_even
st.write('yah')

list_1= [i for i in range(10)]
even_list=return_even(list_1)
st.write (even_list)
