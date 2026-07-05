import streamlit as st

def show_transcript(transcript):
    
    st.markdown(
        f"""
        <div class="transcript-card">
            <h3>📝 Transcript</h3>
            <p class="transcript-text">{transcript}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


        








