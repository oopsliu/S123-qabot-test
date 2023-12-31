"""Python file to serve as the frontend"""
import streamlit as st
from streamlit_chat import message
import faiss
from langchain import OpenAI
from langchain.chains import VectorDBQAWithSourcesChain
import pickle
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQAWithSourcesChain

# Load the LangChain.
index = faiss.read_index("docs.index")

with open("faiss_store.pkl", "rb") as f:
    store = pickle.load(f)

store.index = index
llm = ChatOpenAI(model_name="gpt-4", temperature=0, max_tokens=1000)
# chain = VectorDBQAWithSourcesChain.from_llm(llm=llm, vectorstore=store)
chain = RetrievalQAWithSourcesChain.from_chain_type(llm=llm, retriever=store.as_retriever())


# From here down is all the StreamLit UI.
st.set_page_config(page_title="S123 QA Bot", page_icon=":robot:")
st.header("S123 QA Bot")

if "generated" not in st.session_state:
    st.session_state["generated"] = []

if "past" not in st.session_state:
    st.session_state["past"] = []


def get_text():
    input_text = st.text_input("You: ", "What is Survey123?", key="input")
    return input_text


user_input = get_text()

if user_input:
    result = chain({"question": user_input})
    output = f"Answer: {result['answer']}\nSources: {result['sources']}"

    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state["generated"]:

    for i in range(len(st.session_state["generated"]) - 1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")
