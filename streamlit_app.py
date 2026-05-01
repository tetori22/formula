import streamlit as st

st.title("MatematiX 📐")

with open("matematix.html", "r", encoding="utf-8") as f:
    html_code = f.read()

st.components.v1.html(html_code, height=700)
