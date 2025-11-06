import streamlit as st
from utils.api import call_api
from utils.pdf_utils import extract_text_from_pdf

st.title("🧱 Smart Summary")

uploaded = st.file_uploader("📄 Upload Research Paper", type=["pdf"])

if uploaded:
    analyze = st.button("🔍 Analyze Paper")
    voice = st.button("🔊 Generate Voice Summary")

    if analyze:
        with st.spinner("Analyzing paper..."):
            st.session_state.paper_name = uploaded.name
            st.session_state.paper_text = extract_text_from_pdf(uploaded)
            payload = {"text": st.session_state.paper_text}
            st.session_state.summary = call_api("/summarize", payload)
            st.session_state.insights = call_api("/extract", payload)
        st.success("Summary generated successfully ✅")

    if voice:
        with st.spinner("Generating voice summary..."):
            tts = call_api("/tts", {"text": st.session_state.paper_text})
        st.markdown(f"[🎧 Listen to Voice Summary]({tts.get('audio_url', '#')})")

if "summary" in st.session_state and st.session_state.summary:
    s = st.session_state.summary
    st.markdown("#### 🧠 AI Summary")
    with st.expander("TL;DR Summary", expanded=True):
        st.write(s.get("tldr", ""))
    with st.expander("Abstract Summary"):
        st.write(s.get("abstract", ""))
    with st.expander("Methodology Overview"):
        st.write(s.get("methodology", ""))
    with st.expander("Results & Findings"):
        st.write(s.get("results", ""))
    with st.expander("Limitations"):
        st.write(s.get("limitations", ""))
