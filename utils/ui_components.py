import streamlit as st

def load_css(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def title_banner():
    st.markdown("""
        <div class='pp-banner'>
            <h1 class='pp-title'>📄 PaperPulse – Your AI Research Companion</h1>
            <p class='pp-tagline'>Summarize. Simplify. Discover.</p>
        </div>
    """, unsafe_allow_html=True)
