import streamlit
import pandas as pd
streamlit.title('My Parents New Healthy Dinner')
streamlit.header('Breakfast menu')
streamlit.text('Omega 3 & Blueberry otamale ')
streamlit.text('kale,spinich & rocket Smoothiee')
streamlit.text('hard bolied freerange egg')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)
