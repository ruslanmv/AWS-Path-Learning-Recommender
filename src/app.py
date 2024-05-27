
import streamlit as st
from assistant import ask_assistant
# Create an instruction text
instruction_text = "Hello! I am your AWS Certifications learning path recommender. Please insert only your current role and a description of your role."

# Create a Streamlit app
st.title("AWS Certifications Learning Path Recommender")
# Ask the user for their role
role = st.text_input(label="Insert your current role: ")
# Ask the user for their job description
role_description = st.text_area(label="Briefly describe your job:", height=100)
# Create a submit button
submitted = st.button("Submit")
if submitted:
    # Append the two answers into a single string
    input_text = f"{role} {role_description}"
    # Call the ask_assistant function with the input text
    answer = ask_assistant(input_text)
    # Display the answer from the assistant
    st.write(answer)
else:
    st.write(instruction_text)
