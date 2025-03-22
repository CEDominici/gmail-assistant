import streamlit as st
import subprocess

# --- Streamlit page configuration ---
st.set_page_config(page_title="AI Email Assistant", layout="centered")
st.title("AI Email Assistant (MVP)")

# --- OpenAI API Key Input Section ---
api_key = st.text_input("Paste your OpenAI API Key", type="password")
if st.button("Save Key"):
    # Save the key to a local file for use in scripts
    with open("openai_key.txt", "w") as f:
        f.write(api_key)
    st.success("API Key saved locally.")

# --- Step 1: Gmail OAuth Credential Upload Section ---
st.subheader("Step 1: Upload your Google OAuth credentials JSON file")

# File uploader: lets the user upload their `credentials.json` file
uploaded_file = st.file_uploader("Choose your `credentials.json` file", type=["json"])

if uploaded_file is not None:
    try:
        # Save the uploaded file to the project root as `credentials.json`
        with open("credentials.json", "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success("Credentials file saved successfully!")
    except Exception as e:
        # Display any error that happens during file save
        st.error(f"Failed to save file: {e}")

# --- Step 2: Gmail OAuth Trigger Button ---
st.subheader("Gmail Integration")
if st.button("Authenticate with Gmail"):
    # This will be connected to real Gmail auth logic
    st.info("Gmail auth flow not yet implemented.")

# --- Section 1: Fetch historical email data for training ---
st.subheader("1. Fetch Email Data for Training")
if st.button("Run Fetch + Save to local JSONL"):
    st.info("Running email fetch script...")
    subprocess.run(["python3", "scripts/fetch_emails.py"])
    st.success("Saved training data to data/email_training.jsonl")

# --- Section 2: Generate AI Drafts for unread emails ---
st.subheader("2. Generate Drafts for Unread Emails")
if st.button("Run AI Drafting"):
    st.info("Drafting replies...")
    subprocess.run(["python3", "scripts/create_drafts.py"])
    st.success("Drafts created (simulated).")

# --- Section 3: Extract and update structured data from emails ---
st.subheader("3. Extract & Update Structured Data")
if st.button("Run Extraction + Save to Local Database"):
    st.info("Extracting structured info...")
    subprocess.run(["python3", "scripts/extract_data.py"])
    st.success("Updated local database files.")

# --- Footer: Status panel (placeholder) ---
st.markdown("---")
st.markdown("**Last Sync:** Coming Soon")
st.markdown("**Emails Processed:** Coming Soon")
