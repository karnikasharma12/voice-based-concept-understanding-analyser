import streamlit as st

def add_space(height=25):
    st.markdown(
        f"<div style='height:{height}px;'></div>",
        unsafe_allow_html=True
    )