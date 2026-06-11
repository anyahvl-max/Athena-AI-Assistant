import streamlit as st
import google.generativeai as genai
genai.configure(api_key="AQ.Ab8RN6L7Ai7Wn0RcWDAxkzT3nStIWrXA_S4hAMZQtBD6vZoMOQ")
model = genai.GenerativeModel("gemini-2.5-flash")
st.set_page_config(
    page_title="Ananya AI Assistant",
    page_icon="🤖",
    layout="centered"
)
st.title("🤖 Ananya AI Assistant")
#New Upgrade 2: Custom Welcome Message
st.markdown("### 👋 Welcome to Ananya AI Assistant")
st.write("---")
# NEW UPGRADE 1: clear chat Button in sidebar
with st.sidebar:
    st.title("⚙️ Settings")
    if st.button("🧹clear chat"):
        st.session_state.messages = []
        st.rerun()
#chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
#Display old messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])  
#user input
prompt = st.chat_input("Type your message...")
if prompt:
    #user message
    st.session_state.messages.append(
        {"role":"user","content":prompt}
    )
    with st.chat_message("user"):
        st.markdown(prompt)
#AI response
    response = model.generate_content(prompt)
    reply = response.text
    st.session_state.messages.append(
        {"role":"assistant","content":reply}
    )
    with st.chat_message("assistant"):
        st.markdown(reply)