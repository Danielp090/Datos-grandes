import streamlit as st
import plotly.express as px
st.title("Mi Segunda publicacion")
st.header("Introduccion")
st.write("Esta es mi primera pagina")
fig=px.bar(x=["A","B","C"],y=[5,6,8])
st.plotly_chart(fig)

