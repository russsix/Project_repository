import streamlit as st
from feature_01 import return_even
st.write('yah')

list_1= [i for i in range(10)]
list_2=return_even (list_1)
st.write (list_2)
