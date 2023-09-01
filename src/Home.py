import streamlit as st


#Config
st.set_page_config(layout="wide", page_icon="💬", page_title="Chatbot Demo 🤖")



#Title
st.markdown(
    """
    <h2 style='text-align: center;'>Survey123 Feature Report QA Bot Demo 🤖</h1>
    """,
    unsafe_allow_html=True,)

st.markdown("---")


#Description
st.markdown(
    """ 
    <h5 style='text-align:center;'>I'm Beiyan, an intelligent chatbot created by combining 
    the strengths of Langchain and Streamlit. I use large language models to provide
    context-sensitive interactions. My goal is to help you better understand your data.
    I support PDF, TXT, CSV 🧠</h5>
    """,
    unsafe_allow_html=True)
st.markdown("---")


#Pages
st.subheader("🚀 Beiyan's Pages")
st.write("""
- **Survey123 Feature Report QA Bot**: Chat on the documentation of the Survey123 feature report
- **Chat with your file**: General chat on data (PDF, TXT,CSV) with a [vectorstore](https://github.com/facebookresearch/faiss) (index useful parts(max 4) for respond to the user) | works with [ConversationalRetrievalChain](https://python.langchain.com/en/latest/modules/chains/index_examples/chat_vector_db.html)
""")
st.markdown("---")







