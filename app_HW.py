import streamlit as st
import numpy as np
import altair as alt
import pandas as pd


df_sales = pd.read_csv('sales_data.csv')


st.set_page_config(layout="wide")

st.image('https://5ypbvxa39ihl3fage541b0i.blob.core.windows.net/media/Frigidaire_Media/Logo/elements-logos-color.svg', width=250) 
st.title('2022 Refrigerator Warranty Claim Data')



st.write(df_sales)
