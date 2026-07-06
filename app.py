import streamlit as st
from components.hero import show_hero
from components.overview import show_overview
from components.upload import show_upload
from components.transcript import show_transcript
from components.analysis import show_analysis
from components.dashboard import show_dashboard
from components.footer import show_footer
from components.charts import show_charts
from components.report import show_report
from components.utils import add_space
from mock_data import mock_result

# -------- For Dummy data --------
USE_MOCK = False

def get_result(audio=None):
    if USE_MOCK:
        return mock_result
    else:
        from modules.backend import analyze
        return analyze(audio)

# ------------ Page Configuration-------------
st.set_page_config(
    page_title="Voice Based Concept Understanding Analyzer",
    page_icon="🎤",
    layout="wide"
)
# Load CSS
def load_css():
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
load_css()
# ---------------- Sidebar ----------------
st.sidebar.markdown("""
<div style="text-align:center;">
<h2 style="color:white;">🎤 VCUA</h2>
<p style="color:#94A3B8;">
    Voice Concept Understanding Analyzer
</p>
</div>
<hr>
""", unsafe_allow_html=True)



st.sidebar.markdown("### 📂 Navigation")

page = st.sidebar.radio(
    "",
    [
        "Home",
        "About Project"
    ]
)

# ---------------- Home Page ----------------
if page == "Home":
    show_hero()
    show_overview()
    add_space(18)


        # -------- Session State --------
    if "analysis_done" not in st.session_state:
        st.session_state.analysis_done = False


  

    # ---------- Dashboard Status ----------
    if st.session_state.analysis_done:

        result = st.session_state.result

        audio_status = "🟢 Uploaded"
        transcript_status = "🟢 Ready"
        ai_score_status = f"🔵 {result['score']}%"
        speech_status = result.get("speech_quality", "🟣 Excellent")

    else:
        audio_status = "🟡 Waiting"
        transcript_status = "🟡 Pending"
        ai_score_status = "⚪ --"
        speech_status = "⚪ --"

    # ----------  Status-Cards ----------
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""
        <div class="status-card blue">
            <div class="status-icon">🎤</div>
            <div class="status-title">Audio</div>
            <div class="status-value">{audio_status}</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="status-card green">
            <div class="status-icon">📝</div>
            <div class="status-title">Transcript</div>
            <div class="status-value">{transcript_status}</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="status-card purple">
            <div class="status-icon">🧠</div>
            <div class="status-title">AI Score</div>
            <div class="status-value">{ai_score_status}</div>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown(f"""
        <div class="status-card orange">
            <div class="status-icon">📊</div>
            <div class="status-title">Speech</div>
            <div class="status-value">{speech_status}</div>
        </div>
        """, unsafe_allow_html=True)
    add_space(18)

    
    #------------- Upload cards ---------------
    col1, col2 = st.columns(2, gap="large")
    with col1:
        audio, analyze, warning_placeholder = show_upload()
    

    # -------- Reset analysis when a new file is uploaded --------
    if "last_file" not in st.session_state:
        st.session_state.last_file = None

    if audio is not None:
        if st.session_state.last_file != audio.name:
            st.session_state.analysis_done = False
            st.session_state.last_file = audio.name

    with col2:
        if st.session_state.analysis_done:
            show_transcript(result["transcript"])
        else:
           st.markdown("""
            <div class="transcript-card">

            <h3>📝 Transcript</h3>

            <p style="
            text-align:center;
            padding:90px 10px;
            color:#9CA3AF;">
            Upload an audio file and click
            <b>Analyze</b>
            <br>
            to generate transcript.
            </p>

            </div>
            """, unsafe_allow_html=True)

        
     #------------ analyze button ----------
    if analyze:
        if audio:
            with st.spinner("🤖 AI is analyzing your audio..."):

                import time
                time.sleep(3)

            result = get_result(audio) # mock_data.py
            st.session_state.result = result
            st.session_state.analysis_done = True
            st.rerun()

        else:
           warning_placeholder.warning("⚠️ Please upload an audio file.")

    if st.session_state.analysis_done:

        result = st.session_state.result # mock_data.py
        
        show_analysis(
            result["score"],
            result["confidence"],
            result["fluency"],
            result["clarity"],
            result["summary"]
        )
        add_space(20)

        show_charts(
            result["score"],
            result["confidence"],
            result["fluency"],
            result["clarity"]
        )
        add_space(20)

        show_dashboard(
            result["score"],
            result["confidence"],
            result["fluency"],
            result["clarity"]
        )
        add_space(20)

        show_report(
            result["score"],
            result["confidence"],
            result["fluency"],
            result["clarity"],
            result["summary"]
        )


        #  Desktop Refresh button 
        add_space(10)
        if st.button("🔄 New Analysis", use_container_width=True):

            st.session_state.analysis_done = False
            st.session_state.last_file = None

            if "audio_upload" in st.session_state:
                del st.session_state["audio_upload"]

            st.rerun()
    
    
    #---------------- About Page ----------------
else:
    st.markdown("""
    <div class="about-card">

    <div class="about-title">
    🎯 Project Objective
    </div>

    <div class="about-text">

    Voice Based Concept Understanding Analyzer is an AI-powered platform developed to evaluate a student's spoken explanation.

    It performs:

    ✔ Speech-to-Text Conversion

    ✔ Concept Understanding Analysis

    ✔ Speech Quality Evaluation

    ✔ AI-based Performance Scoring

    ✔ Final PDF Report Generation

    </div>

    </div>
    """, unsafe_allow_html=True)


 
    #--------- Key Features -------

    st.markdown("""
    <div class="section-title">
    ✨ Key Features
    </div>

    <div class="section-subtitle">
    Explore the major capabilities of the platform.
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="about-card">
            <h3>📝 Speech to Text</h3>
            <p>Convert spoken audio into text automatically.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="about-card">
            <h3>🧠 AI Analysis</h3>
            <p>Analyze concept understanding using Artificial Intelligence.</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="about-card">
            <h3>📊 Performance Report</h3>
            <p>Generate confidence, fluency and clarity report.</p>
        </div>
        """, unsafe_allow_html=True)


    #--------------- Technology Stack -------
    st.markdown("""
    <div class="section-title">
    🛠 Technology Stack
    </div>

    <div class="section-subtitle">
    Technologies used to build this platform.
    </div>
    """, unsafe_allow_html=True)

    t1, t2, t3, t4 = st.columns(4)
    with t1:
        st.markdown('<div class="about-card"><h3>🐍 Python</h3></div>', unsafe_allow_html=True)
    with t2:
        st.markdown('<div class="about-card"><h3>⚡ Streamlit</h3></div>', unsafe_allow_html=True)
    with t3:
        st.markdown('<div class="about-card"><h3>🧠 AI / NLP</h3></div>', unsafe_allow_html=True)
    with t4:
        st.markdown('<div class="about-card"><h3>🎤 Speech Processing</h3></div>', unsafe_allow_html=True)

    #------------- Project Modules ------------
    st.markdown("""
    <div class="section-title">
    🎯 Project Modules
    </div>

    <div class="section-subtitle">
    Core modules of the Voice Based Concept Understanding Analyzer.
    </div>
    """, unsafe_allow_html=True)
    m1, m2, m3, m4, m5 = st.columns(5)
    with m1:
        st.success("🎤\n\nAudio Upload")
    with m2:
        st.info("📝\n\nSpeech-to-Text")
    with m3:
        st.warning("🧠\n\nConcept Analysis")
    with m4:
        st.success("🔊\n\nSpeech Quality")
    with m5:
        st.info("📄\n\nAI Report")


    #--------- Future Scope ------------
    st.markdown("""
    <div class="section-title">
    🚀 Future Scope
    </div>

    <div class="section-subtitle">
    Upcoming enhancements planned for the project.
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="about-card">

     Real-Time Speech Analysis
    <br><br>
     Whisper AI Integration
    <br><br>
     Multi-language Support
    <br><br>
     Student Performance History
    <br><br>
     Teacher Dashboard
    </div>
    """, unsafe_allow_html=True)

    #--------- Project Team ------------
    st.markdown("""
    <div class="section-title">
    👨‍💻 Project Team
    </div>

    <div class="section-subtitle">
    Development responsibilities and team roles.
    </div>
    """, unsafe_allow_html=True)
    m1, m2, m3, m4, m5 = st.columns(5)
    with m1:
        st.info("""**Member 1** :🎨 Frontend(Streamlit UI) 
                                    \n Parul Mathuriya""")
    with m2:
        st.info("""**Member 2** :🎤 Speech-to-Text
                                    \n Manish Sharma""")
    with m3:
        st.info("""**Member 3** :🧠 Semantic Analysis
                                     \n Harshit Soni""")
    with m4:
        st.info("""**Member 4** :🔊 Audio Analysis
                                    \n Pankaj Kumar Jangid""")
    with m5:
        st.info("""**Member 5** :⚙️ Backend
                                     \n Karnika Sharma""") 



#---------------- Footer -------------------------------------------
add_space(15)
show_footer()
add_space(10)

    

 










        






