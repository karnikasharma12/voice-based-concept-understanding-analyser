import streamlit as st

def show_upload():

    with st.container():

        st.markdown("""
        <div class="upload-header">
            <div class="upload-icon">🎙️</div>
            <div class="upload-title">
                Upload Your Voice
            </div>
            <div class="upload-subtitle">
                Upload your explanation in MP3 or WAV format for AI analysis.
            </div>
        </div>
        """, unsafe_allow_html=True)

        audio = st.file_uploader(
            "",
            type=["wav", "mp3"],
            label_visibility="collapsed",
            key="audio_upload"
        )

        if audio is not None:
            st.success("✅ Audio Uploaded Successfully")
            st.markdown("### ▶️ Audio Preview")
            st.audio(audio)

            c1, c2 = st.columns(2)

            with c1:
                st.info(f"📄 **File Name**\n\n{audio.name}")

            with c2:
                st.info(f"📦 **File Size**\n\n{audio.size/1024:.2f} KB")

        analyze = st.button("🚀 Analyze", use_container_width=True)

        

        warning_placeholder = st.empty()



    return audio, analyze, warning_placeholder


   
