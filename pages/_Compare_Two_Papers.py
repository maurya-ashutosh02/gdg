import streamlit as st
import PyPDF2
from utils.api import call_api

st.title("⚖️ Compare Two Papers")
st.caption("Upload two research papers and let Gemini analyze how they differ and overlap.")

def extract_text(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    return "".join([page.extract_text() for page in reader.pages if page.extract_text()])

col1, col2 = st.columns(2)
with col1:
    paper_a = st.file_uploader("📄 Upload Paper A", type=["pdf"], key="a")
with col2:
    paper_b = st.file_uploader("📄 Upload Paper B", type=["pdf"], key="b")

if paper_a and paper_b:
    if st.button("🔍 Compare Papers"):
        with st.spinner("Analyzing and comparing both papers using Gemini..."):
            text_a = extract_text(paper_a)
            text_b = extract_text(paper_b)
            payload = {"text_a": text_a, "text_b": text_b}
            comparison = call_api("/compare", payload)

        if comparison.get("differences") or comparison.get("similarities"):
            st.success("✅ Comparison complete!")

            if "summary" in comparison:
                st.markdown("### 🧠 Overall Summary")
                st.write(comparison["summary"])

            st.markdown("### 🔸 Key Differences")
            for diff in comparison.get("differences", []):
                st.markdown(f"- {diff}")

            st.markdown("### 🔹 Key Similarities")
            for sim in comparison.get("similarities", []):
                st.markdown(f"- {sim}")

        else:
            st.error("Could not generate comparison. Try again with shorter papers or check your Gemini key.")
