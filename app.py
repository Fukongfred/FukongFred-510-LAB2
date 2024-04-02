# app.py
import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

st.set_page_config(
    page_title="Penguins Explorer",
    page_icon="🐧",
    layout="centered", # centered, wide 
    initial_sidebar_state="auto", 
    menu_items=None
)

st.title("🐧 Penguins Explorer")
st.subheader('Introduction')
about= '''
A data analysis application to find out interesting insights about penguins in the Artic.
'''
st.markdown(about)

df = pd.read_csv('https://raw.githubusercontent.com/mcnakhaee/palmerpenguins/master/palmerpenguins/data/penguins.csv')

min_bill_length = df['bill_length_mm'].min()
max_bill_length = df['bill_length_mm'].max()
selected_bill_length = st.slider('Select Bill Length Range', min_bill_length, max_bill_length, (min_bill_length, max_bill_length))

# Filter the dataframe based on the selected bill length range
df = df[(df['bill_length_mm'] >= selected_bill_length[0]) & (df['bill_length_mm'] <= selected_bill_length[1])]

species_filter=st.selectbox(
    "Species", 
    df["species"].unique(),
    index=None)
st.write(f"Selected Species: {species_filter}")
if species_filter:
    df = df[df['species'] == species_filter]

islands_filter=st.multiselect('Island', df["island"].unique())
if islands_filter:
    df = df[df['island'].isin(islands_filter)]

st.write(df)

fig = px.scatter(df, x='bill_length_mm', y='bill_depth_mm', color='species', title='Penguin Bill Length vs Depth')
st.plotly_chart(fig)

fig2 = px.histogram(
    df, 
    x="bill_length_mm"
)
st.plotly_chart(fig2)