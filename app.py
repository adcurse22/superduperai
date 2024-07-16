import streamlit as st
from decouple import config
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

OPENAI_API_KEY = config('OPENAI_API_KEY')

# Initialize the OpenAI LLM with LangChain
llm = OpenAI(api_key=OPENAI_API_KEY)

col1, col2 = st.columns(2)


with col1:
    st.header("Input Question")
    question = st.text_area("Enter your question here:", height=270)
    if st.button("Generate Answer"):
        pass


with col2:
    st.header("Generated Answer")
    answer = st.text_area("Answer:", value=st.session_state.get('generated_answer', ''), height=550)
    if st.button("Generate Video"):
      st.write("Generating video...")



# Display the generated answer if any
if 'generated_answer' in st.session_state:
    st.write(st.session_state.generated_answer)


