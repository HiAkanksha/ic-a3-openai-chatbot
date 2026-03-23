# IC A3 — Builder Bot (OpenAI Chatbot)

This project is a simple conversational chatbot built using **Python**, **Streamlit**, and the **OpenAI API** to create a web-based chat interface that remembers conversation history within a session.[web:15][web:107]

Builder Bot acts like a **practical startup co‑founder**: it helps break ideas into steps, suggests MVPs, and can sketch small code snippets.

---

## Features

- ✅ Web UI built with Streamlit (`streamlit run app.py`)[web:15][web:107]  
- ✅ Conversation history stored using `st.session_state` (memory per browser session)[web:15]  
- ✅ Uses OpenAI’s `gpt-4o-mini` model via the official Python SDK[web:106]  
- ✅ Custom persona: **“Builder Bot – your co‑founder”**  
- ✅ Sidebar description explaining how to use the bot  
- ✅ Basic error handling for missing credits / invalid API key

---

## Tech Stack

- **Language:** Python 3.x  
- **Framework:** Streamlit  
- **API:** OpenAI Python SDK (`openai` package)[web:106]  
- **Config:** `.env` file for `OPENAI_API_KEY` (not committed to GitHub)

---

## Getting Started (Local Setup)

### 1. Clone the repository

```bash
git clone https://github.com/HiAkanksha/ic-a3-openai-chatbot.git
cd ic-a3-openai-chatbot
```

### 2. Install dependencies

Make sure Python and `pip` are installed, then run:

```bash
pip install -r requirements.txt
```

### 3. Set your OpenAI API key

Create a file named `.env` in the project root with:

```env
OPENAI_API_KEY=sk-proj-your-key-here
```

- This key is **not** committed to GitHub because `.env` is listed in `.gitignore`.  
- You can create an API key from the OpenAI dashboard under **API Keys**.[web:9][web:106]

### 4. Run the app

```bash
streamlit run app.py
```

This will open the app in your browser at `http://localhost:8501`.[web:107]

---

## How Builder Bot Works

- The app uses `st.session_state` to store a list of messages (`system`, `user`, and `assistant`).  
- On each user message, the full message history is sent to the OpenAI API so the model can respond with context.[web:15][web:106]  
- A **system message** defines the bot as an energetic, practical co‑founder who:
  - Breaks ideas into concrete steps  
  - Suggests simple MVPs instead of over‑engineering  
  - Often ends replies with a **“Next step”** section

If the OpenAI API call fails (for example, no credits or invalid key), the app shows a friendly error message instead of crashing.

---

## Files in This Project

- `app.py` — Main Streamlit app (UI, chat logic, OpenAI integration)  
- `requirements.txt` — Python dependencies  
- `.gitignore` — Ensures `.env` and other local files are not pushed to GitHub  
- `.env` — **Local only** file that stores your `OPENAI_API_KEY` (not in this repo)

---

## Notes

- To actually get responses from the model, your OpenAI account must have an active API key and sufficient credits.[web:34][web:38]  
- Without credits, the app still runs, but the chatbot will display the custom error message defined in `app.py`.