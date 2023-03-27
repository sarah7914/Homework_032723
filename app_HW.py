import streamlit as st
import numpy as np
import altair as alt
import pandas as pd

df_sales = pd.read_csv('sales_data.csv')


st.set_page_config(layout="wide")

st.image('https://5ypbvxa39ihl3fage541b0i.blob.core.windows.net/media/Frigidaire_Media/Logo/elements-logos-color.svg', width=250) 
st.title('2022 Refrigerator Warranty Claim Data')

types = df_sales['Product_Type'].unique().tolist()
styles = df_sales['Product_Styles'].unique().tolist()

type_choice = st.sidebar.selectbox('Select your refrigerator type:', types)
styles = df_sales['Product_Styles'].loc[df_sales['Product_Type']==type_choice].unique()
style_choice = st.sidebar.selectbox('Select your refrigerator style', styles) 

x_sales=df_sales['Year'].loc[df_sales['Product_Styles']==style_choice]
y_sales=df_sales['Quantity'].loc[df_sales['Product_Styles']==style_choice]

df_new = pd.DataFrame(data=x_sales)
df_new['y_sales']=y_sales
df_new['style']=style_choice

barchart = alt.Chart(df_new, title = f'{style_choice} Refrigerators Sold in the Last 2 Years').mark_bar().encode(
    x='Year:O',
    y=alt.Y('sum(y_sales):Q', title='Quantity Sold')
    )

text = barchart.mark_text(
    align='left',
    baseline='middle',
    dy=-5
).encode(
    text=alt.Y('sum(y_sales):Q', title='Quantity Sold')
)

tick = alt.Chart(df_sales).mark_tick(
    color='red',
    thickness=2,
    size=40 * 0.9
).encode(
    x='Year:O',
    y=alt.Y('sum(Quantity):Q')
)

st.altair_chart((barchart + text + tick), use_container_width=True)
