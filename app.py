import streamlit as st
import requests

st.set_page_config(page_title="WhatsHelpAI", layout="centered")

st.markdown("""
    <style>
    .stChatMessage {
        border-radius: 12px;
        padding: 10px 16px;
        margin-bottom: 8px;
        max-width: 70%;
        font-size: 16px;
        line-height: 1.5;
    }
    .user-msg {
        background-color: #514949;
        margin-left: auto;
        text-align: right;
    }
    .bot-msg {
        background-color: #514949;
        margin-right: auto;
        text-align: left;
        border: 1px solid #ececec;
    }
    .stTextInput>div>div>input {
        border-radius: 20px;
        border: 1px solid #ececec;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("💬 WhatsHelpAI")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "input" not in st.session_state:
    st.session_state.input = ""

def send_message():
    user_input = st.session_state.input
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        try:
            response = requests.post(
                "http://localhost:8000/generate_response",
                json={"input_text": user_input},
                timeout=60
            )

            if response.status_code == 200:
                bot_response = response.json().get("response", "No response from bot.")
            else:
                bot_response = f"Error: {response.status_code} - {response.text}"
        except Exception as e:
            bot_response = f"Error connecting to backend: {e}"

        # Handle dict or string response
        if isinstance(bot_response, dict) and "answer" in bot_response:
            content = bot_response["answer"]
        else:
            content = bot_response

        st.session_state.messages.append({"role": "bot", "content": content})
        st.session_state.input = ""  # This is now safe

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="stChatMessage user-msg">{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="stChatMessage bot-msg">{msg["content"]}</div>', unsafe_allow_html=True)

st.text_input("Type your message...", key="input", label_visibility="collapsed", on_change=send_message)