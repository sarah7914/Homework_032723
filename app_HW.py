import streamlit as st
import numpy as np
import altair as alt
import pandas as pd

df_sales = pd.read_csv('sales_data.csv')


st.set_page_config(layout="wide")

st.image('https://5ypbvxa39ihl3fage541b0i.blob.core.windows.net/media/Frigidaire_Media/Logo/elements-logos-color.svg', width=250) 
st.title('2022 Refrigerator Warranty Claim Data')
st.subheader('_Select a refrigerator type and style on the left to view the quantity sold in the last 2 years_')

#Chart 1
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
    x=alt.X('Year:O', axis=alt.Axis(labelAngle=0)),
    y=alt.Y('sum(y_sales):Q', title='Quantity Sold'),
    tooltip=alt.Tooltip('sum(y_sales):Q', format=",.0f")
    )

text = barchart.mark_text(
    align='left',
    baseline='middle',
    dy=-10
).encode(
    text=alt.Y('sum(y_sales):Q', format=",.0f", title='Quantity Sold')
)

st.altair_chart((barchart + text), use_container_width=True)

#Chart 2

locations = df_sales['Location'].unique().tolist()

st.subheader('_Select a refrigerator manufacturing location to view the quantity produced in the last 2 years_')
location_pick = st.select_slider('Slide the red dot to select a manufacturing location', options=locations)

barchart2 = alt.Chart(df_sales, title = f'Refrigerators Produced from {location_pick} in the Last 2 Years').mark_bar().encode(
    x=alt.X('Year:O', axis=alt.Axis(labelAngle=0)),
    y=alt.Y('sum(Quantity):Q', title='Quantity Produced'),
    tooltip=alt.Tooltip('sum(Quantity):Q', format=",.0f")
    ).transform_filter(df_sales['Location']==location_pick)

text2 = barchart2.mark_text(
    align='left',
    baseline='middle',
    dy=-10
).encode(
    text=alt.Y('sum(Quantity):Q', format=",.0f", title='Quantity Produced')
)

st.altair_chart((barchart2 + text2), use_container_width=True)
