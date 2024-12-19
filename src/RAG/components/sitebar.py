import streamlit as st
from src.RAG.utils.api_utils import upload_document, list_documents, delete_document
from src.RAG.entity.api_enitty import ModelName

def display_sitebar():
    model_options = [model.value for model in ModelName]
    st.sidebar.selectbox("Select Model", options=model_options, key="model")

    st.sidebar.header("Upload Document")
    upload_file = st.sidebar.file_uploader("chose file", type=["pdf", "docx", "html"])

    if upload_file is not None:
        if st.sidebar.button("Upload"):
            with st.spinner("uploading........"):
                upload_response = upload_document(upload_file)
                if upload_response:
                     st.sidebar.success(f"File '{upload_file.name}' uploaded successfully with ID {upload_response['file_id']}.")
                     st.session_state.documents = list_documents()
    #load document
    st.sidebar.header('Uploaded Document')
    if st.sidebar.button("Refresh Document list"):
        with st.spinner("Refreshing.........."):
            st.session_state.documents = list_documents()
    
    if "documents" not in st.session_state:
        st.session_state.documents = list_documents()
    
    documents = st.session_state.documents

    if documents:
        for doc in documents:
            st.sidebar.text(f"{doc['filename']} (ID: {doc['id']}, Uploaded: {doc['upload_timestamp']})")
        selected_file_id = st.sidebar.selectbox("Select a document to delete",  options=[doc['id'] for doc in documents], format_func=lambda x: next(doc['filename'] for doc in documents if doc['id'] == x))
        if st.sidebar.button("Delete Selected Document"):
            with st.spinner("Deleting......"):
                delete_response = delete_document(selected_file_id)
                if delete_response:
                    st.sidebar.success(f"Document with ID {selected_file_id} deleted successfully.")
                    st.session_state.documents = list_documents()  # Refresh the list after deletion
                else:
                    st.sidebar.error(f"Failed to delete document with ID {selected_file_id}.")