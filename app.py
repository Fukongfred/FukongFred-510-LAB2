# app.py
import streamlit as st
import pandas as pd
import seaborn as sns

st.set_page_config(
    page_title="Penguins Explorer",
    page_icon="🐧",
    layout="centered", # centered, wide 
    initial_sidebar_state="auto", 
    menu_items=None
)

st.title("🐧 Penguins Explorer")

df = pd.read_csv('https://raw.githubusercontent.com/mcnakhaee/palmerpenguins/master/palmerpenguins/data/penguins.csv')

st.write(df)