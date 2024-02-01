import streamlit as st
from my_fucniton import calculate_wage

name=st.text_input("name")
# st.write(f'name is {name}')
hour=st.number_input("please write hours: ")
rate=st.number_input("please write grade: ")





if st.button("calculate the wage!"):
    wage=calculate_wage(hour,rate)
    st.write(f'the wage for {name} is {wage}')


