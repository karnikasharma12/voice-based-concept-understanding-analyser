import streamlit as st

def show_overview():

  #----------- System Overview --------------
  st.markdown("""
  <h2 class="section-heading">
   System Overview
  </h2>
  """, unsafe_allow_html=True)


  c1, c2, c3, c4 = st.columns(4)
  with c1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-icon">🎤</div>
            <div class="metric-value">120+</div>
            <div class="metric-title">Audio Files</div>
        </div>
        """, unsafe_allow_html=True)
  with c2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-icon">🧠</div>
            <div class="metric-value">95%</div>
            <div class="metric-title">AI Accuracy</div>
        </div>
        """, unsafe_allow_html=True)
  with c3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-icon">👨‍🎓</div>
            <div class="metric-value">500+</div>
            <div class="metric-title">Students Tested</div>
        </div>
        """, unsafe_allow_html=True)
  with c4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-icon">⚡</div>
            <div class="metric-value">&lt; 5 sec</div>
            <div class="metric-title">Processing Time</div>
        </div>
        """, unsafe_allow_html=True)

  
  # ----------- Project Objective --------------
  st.markdown("""
  <div class="objective-card">
    <div class="objective-title">
      🎯 Project Objective
    </div>
    <div class="objective-text">
      This application analyzes a student's spoken explanation using Artificial Intelligence.
      <br><br>
      ✅ Speech to Text Conversion
      <br>
      ✅ Concept Understanding Analysis
      <br>
      ✅ Speech Quality Analysis
      <br>
      ✅ Overall Performance Evaluation
    </div>
  </div>
  """, unsafe_allow_html=True)










