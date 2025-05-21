import streamlit as st
import plotly.express as px
import pandas as pd
df=pd.read_csv("house_sales.csv")

st.title("Graficas dataset")
st.header("Introduccion")
st.write("Esta es mi primera pagina")
fig=px.bar(x=["A","B","C"],y=[5,6,8])
st.plotly_chart(fig)
st.header("Datos")
fig=px.scatter(df,x="PropertyType",y="SalePrice")
st.plotly_chart(fig)
st.header("Grafica 2")
fig=px.scatter(df,x="SqFtLot",y="SalePrice")
st.plotly_chart(fig)
st.header("Grafica 3")
fig=px.scatter(df,x="YrBuilt",y="SalePrice")
st.plotly_chart(fig)



