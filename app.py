from openai import OpenAI
import streamlit as st

# Initialize OpenAI API
f = open(r"keys/.openai_api_key.txt")
OPENAI_API_KEY = f.read()

# Streamlit UI
st.title("GenAI App - AI Code Reviewer")
st.subheader("Submit your code for expert review and receive actionable feedback instantly!")

client = OpenAI(api_key = OPENAI_API_KEY)

# OPENAI_API_KEY = "Your api key"
# client = OpenAI(api_key=OPENAI_API_KEY)

# Input field for Python code
prompt = st.text_area("Enter your python code here.....", height=220)

# Button to trigger code review
if st.button("Generate") == True:

    # Call OpenAI API for code review
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "As an expert in code review, I'll analyze your code for bugs, errors, and provide corrected versions for improvement."},
        {"role": "user", "content": prompt}
      ]
    )
    st.markdown("<h3 style='color:green;font-size:20px;'>Corrected Code and review:</h3>", unsafe_allow_html=True)
    st.write(response.choices[0].message.content)
