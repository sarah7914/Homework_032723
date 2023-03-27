import streamlit as st
import numpy as np
import altair as alt
import pandas as pd


df_repair = pd.read_csv('repair_data.csv')
df_sales = pd.read_csv('sales_data.csv')


st.set_page_config(layout="wide")

st.image('https://5ypbvxa39ihl3fage541b0i.blob.core.windows.net/media/Frigidaire_Media/Logo/elements-logos-color.svg', width=250) 
st.title('2022 Refrigerator Warranty Claim Data')

types = df_sales['Product_Type'].drop_duplicates()
styles = df_sales['Product_Styles'].drop_duplicates()

type_choice = st.sidebar.selectbox('Select your refrigerator type:', types)
styles = df_sales['Product_Styles'].loc[df_sales['Product_Type']==type_choice].unique()
style_choice = st.sidebar.selectbox('Select your refrigerator style', styles) 

x_sales=df_sales['Year'].loc[df_sales['Product_Styles']==style_choice]
y_sales=df_sales['Quantity'].loc[df_sales['Product_Styles']==style_choice]

df_new = pd.DataFrame(data=x_sales)
df_new['y_sales']=y_sales
df_new['style']=style_choice

barchart = alt.Chart(df_new).mark_bar().encode(
    x='Year:O',
    y='sum(y_sales):Q', 
    color='style:O'
)


text = barchart.mark_text(
    align='left',
    baseline='middle',
    dx=10  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text='sum(y_sales):Q'
)

st.altair_chart((barchart + text), use_container_width=True)
