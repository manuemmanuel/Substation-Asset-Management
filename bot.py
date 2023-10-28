import streamlit as st
import spacy
nlp = spacy.load("en_core_web_sm")
from data import patterns, responses
def chatbot_response(input_text):
    nlp(input_text.lower())
    for category, patterns_list in patterns.items():
        for pattern in patterns_list:
            if pattern in input_text.lower():
                return responses[category]
    return "I'm sorry, I don't understand that. Please ask about test procedures, acceptable limits, issue resolution, safety guidelines, or equipment recommendations."
st.title("Substation Asset Maintenance Chatbot")
user_input = st.text_input("User: ")
if user_input:
    response = chatbot_response(user_input)
    st.text("response: " + response)
if st.button("Quit"):
    st.text("response: Goodbye! Have a great day!")
