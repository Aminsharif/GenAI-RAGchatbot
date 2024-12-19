import streamlit as st
from src.RAG.utils.api_utils import get_api_response

def display_chat_Interface():
    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.markdown(message['content'])

    if prompt:= st.chat_input("Query:"):
        st.session_state.messages.append({"role":"user", "content": prompt})
        with st.chat_message('user'):
            st.markdown(prompt)
        
        with st.spinner('Getting response....'):
            response = get_api_response(prompt, st.session_state.session_id, st.session_state.model)

            if response:
                st.session_state.sesion_id = response.get("session_id")
                st.session_state.messages.append({'role':'assistant', 'content': response['answer']})

                with st.chat_message('assistant'):
                    st.markdown(response['answer'])

                    with st.expander("Details"):
                        st.subheader("Generated Answer")
                        st.code(response['answer'])
                        st.subheader('Model Used')
                        st.code(response['model'])
                        st.subheader("Session Id")
                        st.code(response['session_id'])
            else:
                st.error("Failed to get a response from the API. Please try again.")