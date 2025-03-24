import streamlit as st
import streamlit.components.v1 as components
import subprocess
import os

# --- Page config must be first ---
st.set_page_config(page_title="AI Email Assistant", layout="centered")

# --- Inject secure HTML/JS (includes blinking log and localStorage logic) ---
if os.path.exists("secure_local_storage_ui.html"):
    components.html(open("secure_local_storage_ui.html").read(), height=0)

# --- Helper for logging to frontend log ---
def frontend_log(message):
    log_script = f"""
    <script>
      window.typeLogEntry?.("[{time.strftime('%H:%M:%S')}] {message}");
    </script>
    """
    components.html(log_script, height=0)

# --- Login Screen ---
if "unlocked" not in st.session_state:
    st.title("🔐 Login to AI Email Assistant")

    passphrase = st.text_input("Passphrase", type="password")
    api_key = st.text_input("OpenAI API Key", type="password")
    uploaded_file = st.file_uploader("Upload Gmail credentials.json", type="json")

    col1, col2 = st.columns([2, 1])
    with col1:
        if st.button("Login & Save"):
            if not passphrase or not api_key or not uploaded_file:
                st.error("All fields are required.")
            else:
                gmail_json = uploaded_file.read().decode("utf-8").replace("\\", "\\\\").replace('"', '\\"')
                st.session_state["unlocked"] = True
                st.session_state["passphrase"] = passphrase

                # Save API Key
                components.html(f"""
                <script>
                  window.AIEmailSecureStorage.saveEncrypted("openai_api_key", "{api_key}", "{passphrase}");
                  window.AIEmailSecureStorage.saveEncrypted("gmail_credentials", JSON.parse("{gmail_json}"), "{passphrase}");
                  window.typeLogEntry?.("[00:00:00] Credentials saved and encrypted.");
                </script>
                """, height=0)
                st.rerun()

    with col2:
        if st.button("🧼 Clear & Restart"):
            st.session_state.clear()
            components.html("<script>window.AIEmailSecureStorage.clearAllCredentials();</script>", height=0)
            st.rerun()

    st.markdown("---")
    st.markdown("### System Log")
    components.html("<div id='log-container'></div>", height=150)
    st.stop()

# --- Main Dashboard ---
st.title("📬 AI Email Assistant Dashboard")

# --- Section: Gmail Auth Placeholder ---
st.subheader("Gmail Integration")
if st.button("Authenticate with Gmail"):
    st.info("Gmail auth flow not yet implemented.")
    frontend_log("[00:00:00] Gmail auth attempted.")

# --- Section 1: Fetch historical email data for training ---
st.subheader("1. Fetch Email Data for Training")
if st.button("Run Fetch + Save to local JSONL"):
    st.info("Running email fetch script...")
    subprocess.run(["python3", "scripts/fetch_emails.py"])
    st.success("Saved training data to data/email_training.jsonl")
    frontend_log("[00:00:00] Email fetch script executed.")

# --- Section 2: Generate AI Drafts ---
st.subheader("2. Generate Drafts for Unread Emails")
if st.button("Run AI Drafting"):
    st.info("Drafting replies...")
    subprocess.run(["python3", "scripts/create_drafts.py"])
    st.success("Drafts created (simulated).")
    frontend_log("[00:00:00] Drafts created for unread emails.")

# --- Section 3: Extract and update structured data ---
st.subheader("3. Extract & Update Structured Data")
if st.button("Run Extraction + Save to Local Database"):
    st.info("Extracting structured info...")
    subprocess.run(["python3", "scripts/extract_data.py"])
    st.success("Updated local database files.")
    frontend_log("[00:00:00] Structured data extracted and saved.")

# --- Footer Log Panel ---
st.markdown("---")
st.markdown("### System Log")
components.html("<div id='log-container'></div>", height=150)
