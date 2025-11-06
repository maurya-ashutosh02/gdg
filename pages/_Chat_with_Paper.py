import streamlit as st
from utils.api import call_api

st.title("💬 Chat with Paper")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "paper_text" not in st.session_state or not st.session_state.paper_text:
    st.warning("Upload a paper in the Smart Summary tab first.")
else:
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("Ask anything about this paper...")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.spinner("Thinking..."):
            resp = call_api("/chat", {"query": user_input, "context": st.session_state.paper_text})
        answer = resp.get("answer", "Sorry, no response.")
        st.session_state.messages.append({"role": "assistant", "content": answer})
        with st.chat_message("assistant"):
            st.markdown(answer)
