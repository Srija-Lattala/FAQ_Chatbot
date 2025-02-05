import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Get the Gemini API key from the environment variables
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("GOOGLE_API_KEY not found in environment variables. Please check your .env file.")
    st.stop()

# Set the API key as an environment variable
os.environ["GOOGLE_API_KEY"] = api_key

# Initialize the Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.7)

# List of FAQs and their answers (can be extended for other topics)
faq_data = {
    "What is Python?": "Python is a high-level, interpreted programming language known for its ease of use and readability. It is widely used for web development, data analysis, artificial intelligence, and more.",
    "How do I install Python?": "You can download Python from the official website: https://www.python.org/downloads/. Once downloaded, you can install it by running the installer and following the instructions.",
    "What are Python data types?": "Python has several built-in data types, including integers, floats, strings, lists, tuples, sets, and dictionaries.",
    "What is a function in Python?": "A function in Python is a block of reusable code that performs a specific task. Functions are defined using the 'def' keyword.",
    "What is a list in Python?": "A list in Python is a collection of items in a particular order. Lists are mutable, meaning you can change their contents after creation.",
}

# Streamlit app
def main():
    st.title("FAQ Chatbot: Python Programming")
    st.subheader("Ask any Python-related question, and I'll try to provide an answer!")

    # User input
    user_question = st.text_input("Ask a question about Python:")

    if user_question:
        # Create a prompt template
        template = """
        You are an AI assistant trained on Python programming. Please answer the user's question as accurately as possible, based on the following FAQ dataset:

        FAQ Data:
        {faq_data}

        User's Question:
        "{user_question}"

        Answer:
        """

        prompt = PromptTemplate(
            input_variables=["faq_data", "user_question"],
            template=template
        )

        # Format the prompt with the FAQ data and user question
        formatted_prompt = prompt.format(
            faq_data="\n".join([f"{q}: {a}" for q, a in faq_data.items()]),
            user_question=user_question
        )

        # Get the response from the model
        with st.spinner("Fetching answer..."):
            response = llm.invoke(formatted_prompt)

        # Display the answer
        if response.content:
            st.success("Answer:")
            st.text(response.content)
        else:
            st.error("Sorry, I couldn't find an answer to that question. Please try another.")

if __name__ == "__main__":
    main()
