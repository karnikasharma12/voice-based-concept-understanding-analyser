import streamlit as st

def show_dashboard(score, confidence, fluency, clarity):

    overall = (score + confidence + fluency + clarity) / 4

    if overall >= 90:
        performance = "Excellent ⭐⭐⭐⭐⭐"
    elif overall >= 75:
        performance = "Very Good ⭐⭐⭐⭐"
    elif overall >= 60:
        performance = "Good ⭐⭐⭐"
    else:
        performance = "Needs Improvement ⭐⭐"

    st.markdown(f"""
    <div class="evaluation-card">

    <h3>📋 Final Evaluation</h3>

    <p><b>Overall Performance :</b> {performance}</p>

    <p><b>Concept Score :</b> {score}%</p>

    <p><b>Confidence :</b> {confidence}%</p>

    <p><b>Fluency :</b> {fluency}%</p>

    <p><b>Clarity :</b> {clarity}%</p>

    <p><b>Recommendation :</b> Continue practicing to further improve communication skills.</p>

    </div>
    """, unsafe_allow_html=True)