import streamlit as st

Num = st.number_input("Write any number", step=1)
i = 1
if Num:
  while(i<11):
   st.write(Num*i)
   i=i+1