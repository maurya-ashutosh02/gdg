# app.py
import streamlit as st
from utils.ui_components import load_css, title_banner
from utils.pdf_utils import extract_text_from_pdf
from utils.api import call_api
import io

# Page configuration
st.set_page_config(
    page_title="PaperPulse – Your AI Research Companion",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load CSS
load_css("assets/styles.css")

# Title Banner
title_banner()

# Sidebar
st.sidebar.image("assets/logo.jpg", width=70)
st.sidebar.title("PaperPulse")
st.sidebar.caption("Your AI Research Companion")

if st.sidebar.button("🔁 Reset Chat"):
    st.session_state.messages = []
    st.toast("Chat reset", icon="✅")

st.sidebar.markdown("---")
st.sidebar.markdown("**Navigate using tabs above 👆**")
st.sidebar.markdown("---")
with st.sidebar.expander("ℹ️ About PaperPulse"):
    st.markdown("""
    **PaperPulse** helps you **summarize**, **chat**, and **discover**
    insights from research papers.  
    Upload PDFs, ask questions, and explore AI-generated insights.
    """)

st.markdown("Welcome to **PaperPulse** 👋 — head to the tabs to begin.")
