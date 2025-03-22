import streamlit as st
import streamlit.components.v1 as components
import subprocess

# 🚨 THIS MUST COME FIRST!
st.set_page_config(page_title="AI Email Assistant", layout="centered")

# Inject custom HTML/JS (encryption logic + background video)
components.html(open("secure_local_storage_ui.html").read(), height=0)

st.title("AI Email Assistant (MVP)")

# --- Passphrase Entry (required) ---
st.subheader("🔐 Enter Your Encryption Passphrase")

if "unlocked" not in st.session_state:
    passphrase = st.text_input("Enter your passphrase to unlock credentials", type="password")
   if st.button("Unlock"):
    if passphrase != "":
        st.session_state["passphrase"] = passphrase
        st.session_state["unlocked"] = True
        st.rerun()
    else:
        st.warning("Passphrase is required to proceed.")

# --- Section: OpenAI API Key ---
st.subheader("Step 1: Enter Your OpenAI API Key")
api_key = st.text_input("Paste your OpenAI API Key", type="password")
if st.button("🔒 Save API Key Securely"):
    components.html(f"""
    <script>
      window.AIEmailSecureStorage.saveEncrypted("openai_api_key", "{api_key}", "{st.session_state['passphrase']}");
    </script>
    """, height=0)
    st.success("API Key saved to secure local storage.")

# --- Section: Gmail JSON Upload ---
st.subheader("Step 2: Upload Gmail OAuth JSON (credentials.json)")
uploaded_file = st.file_uploader("Upload your credentials.json file", type=["json"])

if uploaded_file is not None:
    gmail_json = uploaded_file.read().decode("utf-8").replace("\\", "\\\\").replace('"', '\\"')
    if st.button("🔒 Save Gmail Credentials Securely"):
        components.html(f"""
        <script>
          const creds = JSON.parse("{gmail_json}");
          window.AIEmailSecureStorage.saveEncrypted("gmail_credentials", creds, "{st.session_state['passphrase']}");
        </script>
        """, height=0)
        st.success("Gmail credentials saved to secure local storage.")

# --- Gmail Auth Placeholder ---
st.subheader("Gmail Integration")
if st.button("Authenticate with Gmail"):
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

# --- Footer: Status panel ---
st.markdown("---")
st.markdown("**Last Sync:** Coming Soon")
st.markdown("**Emails Processed:** Coming Soon")
