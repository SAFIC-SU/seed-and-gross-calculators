import streamlit as st
import os

def load_css():
    css_path = os.path.join("assets", "css", "app.css") 
    with open(css_path, "r", encoding="utf-8") as f:  
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
