import streamlit as st
from src.utils import call_llama


st.title(":zap: Llama 3.2 chatbot")
st.caption(":llama: A Streamlit app powered by Llama 3.2")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    with st.spinner("Generating response..."):
        response = call_llama("llama3.2", prompt)
        msg = response['response'] #if isinstance(response, dict) else response
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)