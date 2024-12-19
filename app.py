import streamlit as st
from src.RAG.components.sitebar import display_sitebar
from src.RAG.components.chat_interface import display_chat_Interface

st.title("LangChain RAG Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "session_id" not in st.session_state:
    st.session_state.session_id = None

display_sitebar()

display_chat_Interface()