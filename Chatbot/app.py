import os
from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser



# Load environment variables
load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Set up the LLM with Groq API
llm = ChatGroq(model="llama3-70b-8192", api_key=GROQ_API_KEY)

# Define the prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an AI assistant specialized in helping users optimize their LinkedIn profiles, create engaging posts, and network effectively."),
    ("user", "Question: {question}")
])

# Output parser
output_parser = StrOutputParser()

# Create the chain
chain = prompt | llm | output_parser

# Streamlit UI
st.title("LinkedIn Optimization AI Chatbot")
input_text = st.text_input("Ask about LinkedIn strategies, post ideas, or profile improvements")

if input_text:
    response = chain.invoke({"question": input_text})
    st.subheader("AI Response:")
    st.write(response)
    
    st.write("💡 Tip: Keep your LinkedIn profile updated and engage with your network regularly for better visibility!")