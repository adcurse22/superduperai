# import streamlit as st
# from decouple import config
# from langchain.chains import LLMChain
# from langchain.prompts import PromptTemplate
# from langchain.memory import ConversationBufferWindowMemory
# from langchain.chat_models import ChatOpenAI
#
# prompt = PromptTemplate(
#     input_variables=["chat_history", "question"],
#     template="""You are a very kind and friendly AI assistant. You are
#     currently having a conversation with a human. Answer the questions
#     in a kind and friendly tone.
#
#     chat_history: {chat_history},
#     Human: {question}
#     AI:"""
# )
# llm = ChatOpenAI(openai_api_key=config("OPENAI_API_KEY"),max_tokens=150)
#
# memory = ConversationBufferWindowMemory(memory_key='chat_history',k=4)
#
# llm_chain = LLMChain(
#     llm=llm,
#     memory=memory,
#     prompt=prompt
# )
#
#
#
# col1, col2 = st.columns(2)
#
# if "messages" not in st.session_state.keys():
#     st.session_state.messages = [
#         {"role": "assistant", "content": "Hello there, I'm a ChatGPT clone"}
#     ]
#
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.write(message["content"])
#
#
# with col1:
#     st.header("Input Question")
#     question = st.text_area("Enter your question here:", height=270)
#     user_prompt = question
#
# with col2:
#     st.header("Generated Answer")
#     answer = st.text_area("Answer:", value=st.session_state.get('generated_answer', ''), height=550)
#
# if user_prompt is not None:
#     st.session_state.messages.append({"role": "user", "content": user_prompt})
#     with st.chat_message("user"):
#         st.write(user_prompt)
#
#     if st.session_state.messages[-1]["role"] != "assistant":
#         with st.chat_message("assistant"):
#             with st.spinner("Loading..."):
#                 try:
#                     ai_response = llm_chain.predict(question=user_prompt)
#                 except Exception as e:
#                     if "rate limit" in str(e).lower():
#                         ai_response = "Rate limit exceeded: please try again later."
#                     else:
#                         ai_response = f"An error occurred: {str(e)}"
#                     st.error(ai_response)
#                 st.write(ai_response)
#         new_ai_message = {"role": "assistant", "content": ai_response}
#         st.session_state.messages.append

import streamlit as st
from decouple import config
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferWindowMemory
from langchain.chat_models import ChatOpenAI

# Prompt template
prompt = PromptTemplate(
    input_variables=["chat_history", "question"],
    template="""You are a very kind and friendly AI assistant. You are
    currently having a conversation with a human. Answer the questions
    in a kind and friendly tone.

    chat_history: {chat_history},
    Human: {question}
    AI:"""
)

# Initialize OpenAI LLM with LangChain, with a token limit
llm = ChatOpenAI(openai_api_key=config("OPENAI_API_KEY"), max_tokens=150)

# Set up memory
memory = ConversationBufferWindowMemory(memory_key='chat_history', k=4)

# Create an LLM chain
llm_chain = LLMChain(
    llm=llm,
    memory=memory,
    prompt=prompt
)

# Initialize session state for messages and generated answer
if "messages" not in st.session_state:
    st.session_state.messages = []

if "generated_answer" not in st.session_state:
    st.session_state.generated_answer = ""

# Layout with two columns
col1, col2 = st.columns(2)

with col1:
    st.header("Input Question")
    question = st.text_area("Enter your question here:", height=270)
    generate_button = st.button("Generate")

if generate_button and question:
    user_prompt = question
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    with st.spinner("Loading..."):
        try:
            ai_response = llm_chain.predict(question=user_prompt)
        except Exception as e:
            if "rate limit" in str(e).lower():
                ai_response = "Rate limit exceeded: please try again later."
            else:
                ai_response = f"An error occurred: {str(e)}"
            st.error(ai_response)

        st.session_state.generated_answer = ai_response  # Update generated answer in session state

    new_ai_message = {"role": "assistant", "content": ai_response}
    st.session_state.messages.append(new_ai_message)

# Update the Generated Answer section with the latest response
st.text_area("Answer:", value=st.session_state['generated_answer'], height=550, key='generated_answer_area')
