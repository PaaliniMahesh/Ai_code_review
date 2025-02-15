import google.generativeai as genai
import streamlit as st

# Configure API Key
genai.configure(api_key="AIzaSyDLQ_21-2FgM1-qsKaFI7sfWCC8YdE9qtM")

# Streamlit UI
st.title('AI Code Review')


# user input
user_prompt=st.text_area('Enter your code')
# process ai review

if st.button("code Review"):
    if user_prompt.strip():
# System Instruction for AI Model
        system_prompt = """
    Given a Python, C, C++, SQL, or Java code snippet, analyze the submitted code and identify bugs, errors, or areas of improvement.
    Provide the fixed code and explain the reasoning behind the corrections or suggestions.
    """

# Load Generative AI Model
        model = genai.GenerativeModel(model_name='models/gemini-2.0-flash-exp',
                              system_instruction=system_prompt)
        response=model.generate_content(user_prompt)

        st.subheader("AI Review")
        st.write(response.text)
    else:
        st.warning("please eneter some code to review")



