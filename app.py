# ── 1. IMPORTS ──────────────────────────────────────────────────────────────
# streamlit builds the web UI; openai talks to GPT; dotenv loads your API key
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# ── 2. LOAD API KEY FROM .env FILE ───────────────────────────────────────────
# This reads your secret key from the .env file so it's never hardcoded
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ── 3. PAGE CONFIG ───────────────────────────────────────────────────────────
# Sets the browser tab title and icon
st.set_page_config(page_title="IC A3 — Builder Bot", page_icon="🚀")
st.title("🚀 Builder Bot — Your Co‑founder")
st.caption("IC Assignment 3 · Action‑oriented chatbot for shipping MVPs")

# ── 3b. SIDEBAR DESCRIPTION ─────────────────────────────────────────────────
# Sidebar explains what this bot is and how to use it
with st.sidebar:
    st.subheader("👥 About Builder Bot")
    st.write(
        "Builder Bot is an action‑oriented co‑founder assistant.\n\n"
        "- Helps you break ideas into shippable steps\n"
        "- Suggests simple MVPs instead of over‑engineering\n"
        "- Can sketch small code snippets to get you started\n\n"
        "Use it like you would use a startup co‑founder when you're stuck."
    )

# ── 4. SESSION STATE (MEMORY) ────────────────────────────────────────────────
# st.session_state stores data that persists as long as the browser tab is open.
# Without this, the chat history would reset on every message.
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": (
                "You are Builder Bot, an energetic, practical startup co‑founder. "
                "You help the user ship things: break ideas into concrete steps, "
                "suggest simple MVPs, and provide small code skeletons when helpful. "
                "Be action‑oriented, avoid long theory, and end most replies with a clear "
                "section titled 'Next step' for the user."
            )
        }
    ]

# ── 5. DISPLAY EXISTING CHAT HISTORY ─────────────────────────────────────────
# Loop through all past messages and render them in the chat UI.
# We skip the first 'system' message — it's instructions for the AI, not for display.
for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ── 6. HANDLE NEW USER INPUT ─────────────────────────────────────────────────
# st.chat_input() shows the text box at the bottom. It returns whatever the user typed.
if user_input := st.chat_input("Describe what you want to build..."):

    # Add the user's message to our history list
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Show the user's message immediately in the chat
    with st.chat_message("user"):
        st.markdown(user_input)

    # ── 7. CALL OPENAI API (WITH ERROR HANDLING) ─────────────────────────────
    # We send the ENTIRE messages list every time. This is how the AI "remembers"
    # the conversation — it sees all previous messages on every call.
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",   # Fast and cheap model, great for beginners
                    messages=st.session_state.messages,
                    temperature=0.7,       # 0 = robotic, 1 = creative. 0.7 is balanced.
                    max_tokens=1000        # Max length of the AI's reply
                )

                # Extract the text from the response object
                assistant_reply = response.choices[0].message.content

            except Exception as e:
                # If something goes wrong (no credits, bad key, network, etc.)
                assistant_reply = (
                    "⚠️ I ran into an error while talking to the OpenAI API.\n\n"
                    "Common reasons:\n"
                    "- No billing/credits set up on your OpenAI account\n"
                    "- Invalid or missing `OPENAI_API_KEY` in your `.env` file\n\n"
                    "Technical details (for debugging):\n"
                    f"`{e}`"
                )

        # Display the reply (either normal answer or error message)
        st.markdown(assistant_reply)

    # ── 8. SAVE ASSISTANT REPLY TO HISTORY ────────────────────────────────────
    # Add the AI's reply to history so future calls include it as context
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})