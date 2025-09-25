# Web-based chatbot using Streamlit
import streamlit as st
import time

class WebChatBot:
    def __init__(self):
        self.responses = {
            "hello": "Hi there! How can I help you?",
            "hi": "Hello! What can I do for you?",
            "how are you": "I'm doing great! How about you?",
            "thanks": "You're welcome!",
            "bye": "Have a great day!"
        }
    
    def get_response(self, message):
        message = message.lower().strip()
        for key in self.responses:
            if key in message:
                return self.responses[key]
        return "I'm still learning! Can you rephrase that?"

# Streamlit app
st.title("Python Web Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What would you like to chat about?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    chatbot = WebChatBot()
    response = chatbot.get_response(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
