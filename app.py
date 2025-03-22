
import streamlit as st
import subprocess

st.set_page_config(page_title="AI Email Assistant", layout="centered")
st.title("AI Email Assistant (MVP)")

# --- API Key input
api_key = st.text_input("Paste your OpenAI API Key", type="password")
if st.button("Save Key"):
    with open("openai_key.txt", "w") as f:
        f.write(api_key)
    st.success("API Key saved locally.")

# --- Gmail Auth Placeholder
st.subheader("Gmail Integration")
if st.button("Authenticate with Gmail"):
    st.info("Gmail auth flow not yet implemented.")

# --- Section 1: Fetch historical data
st.subheader("1. Fetch Email Data for Training")
if st.button("Run Fetch + Save to local JSONL"):
    st.info("Running email fetch script...")
    subprocess.run(["python3", "scripts/fetch_emails.py"])
    st.success("Saved training data to data/email_training.jsonl")

# --- Section 2: Generate AI Drafts
st.subheader("2. Generate Drafts for Unread Emails")
if st.button("Run AI Drafting"):
    st.info("Drafting replies...")
    subprocess.run(["python3", "scripts/create_drafts.py"])
    st.success("Drafts created (simulated).")

# --- Section 3: Extract structured data
st.subheader("3. Extract & Update Structured Data")
if st.button("Run Extraction + Save to Local Database"):
    st.info("Extracting structured info...")
    subprocess.run(["python3", "scripts/extract_data.py"])
    st.success("Updated local database files.")

# --- Status panel
st.markdown("---")
st.markdown("**Last Sync:** Coming Soon")
st.markdown("**Emails Processed:** Coming Soon")
