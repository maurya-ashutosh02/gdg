import streamlit as st
from utils.api import call_api
import json

st.title("🔍 Insights & Future Work")

if "insights" not in st.session_state or not st.session_state.insights:
    st.info("Run analysis in Smart Summary first.")
else:
    ins = st.session_state.insights
    st.markdown("#### 🧩 Insights")
    st.markdown("**Keywords**")
    for kw in ins.get("keywords", []):
        st.markdown(f"<span class='pp-chip'>{kw}</span>", unsafe_allow_html=True)
    st.markdown("**Datasets**")
    for ds in ins.get("datasets", []):
        st.markdown(f"<span class='pp-chip'>{ds}</span>", unsafe_allow_html=True)
    st.markdown("**Algorithms**")
    for al in ins.get("algorithms", []):
        st.markdown(f"<span class='pp-chip'>{al}</span>", unsafe_allow_html=True)

eli15 = st.toggle("🧒 Explain Like I'm 15")
if eli15 and "summary" in st.session_state:
    with st.spinner("Simplifying..."):
        simp = call_api("/simplify", {"text": json.dumps(st.session_state.summary)})
    st.success(simp.get("simplified", ""))

if st.button("🔮 Generate Future Research Suggestions"):
    with st.spinner("Thinking ahead..."):
        fw = call_api("/future-work", {"text": st.session_state.paper_text})
    if fw.get("suggestions"):
        for i, s in enumerate(fw["suggestions"], 1):
            st.markdown(f"- **{i}.** {s}")
