import streamlit as st


def show_analysis(score, confidence, fluency, clarity, summary):

    st.divider()

    # ---------------- Heading ----------------
    st.subheader("📊 AI Analysis Dashboard")

    # ---------------- Overall Score ----------------
    st.markdown("""
    <div class="ai-card">
        <div class="ai-title">
            Overall AI Evaluation
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.progress(score/100)

    st.markdown(f"""
    <div class="overall-score">
        {score}%
    </div>
    """, unsafe_allow_html=True)

    # ---------------- Metric Cards ----------------

    c1, c2 = st.columns(2)

    with c1:

        st.markdown(f"""
        <div class="ai-card">
            <div class="ai-icon">🧠</div>
            <div class="ai-title">Concept Score</div>
            <div class="ai-value">{score}%</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="ai-card">
            <div class="ai-icon">🎤</div>
            <div class="ai-title">Fluency</div>
            <div class="ai-value">{fluency}%</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:

        st.markdown(f"""
        <div class="ai-card">
            <div class="ai-icon">💬</div>
            <div class="ai-title">Confidence</div>
            <div class="ai-value">{confidence}%</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="ai-card">
            <div class="ai-icon">🔊</div>
            <div class="ai-title">Clarity</div>
            <div class="ai-value">{clarity}%</div>
        </div>
        """, unsafe_allow_html=True)

    # ---------------- Summary ----------------

    st.subheader("🧠 AI Generated Summary")

    st.markdown(
        f"""
        <div class="summary-box">
            <h3>Summary</h3>
            <p>{summary}</p>
        </div>
         """,
        unsafe_allow_html=True
    )