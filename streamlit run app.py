import streamlit as st
import os
from pathlib import Path

# ===============================
# Page Config
# ===============================
st.set_page_config(
    page_title="My Work Upload | Shahriar",
    layout="wide"
)

# ===============================
# Hide Streamlit UI
# ===============================
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ===============================
# Login System
# ===============================
def login():
    st.session_state['logged_in'] = False
    with st.form("login_form"):
        st.subheader("Login to Upload")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")
        if submitted:
            if username == "sabuj2025" and password == "sabuj":
                st.success("Login Successful! ✅")
                st.session_state['logged_in'] = True
            else:
                st.error("Invalid Username or Password ❌")

# ===============================
# File Upload + Display
# ===============================
UPLOAD_DIR = Path("my_work_uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

def upload_file():
    st.subheader("Upload Your Work")
    uploaded_file = st.file_uploader("Choose a file", type=["png","jpg","jpeg","pdf","txt"], key="file_uploader")
    if uploaded_file is not None:
        # Save file
        save_path = UPLOAD_DIR / uploaded_file.name
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"Uploaded: {uploaded_file.name} ✅")
        # Animation: confetti
        st.balloons()

def show_my_work():
    st.subheader("My Work Gallery")
    files = list(UPLOAD_DIR.iterdir())
    if not files:
        st.info("No work uploaded yet.")
        return
    for file in files:
        if file.suffix.lower() in [".png", ".jpg", ".jpeg"]:
            st.image(str(file), width=200)
        else:
            st.write(f"- {file.name}")

# ===============================
# Main Logic
# ===============================
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Upload Icon / Button
st.markdown(
    """
    <style>
    .upload-btn {
        background-color:#1976D2;
        color:white;
        padding:10px 15px;
        border-radius:8px;
        cursor:pointer;
        font-weight:bold;
        transition: transform 0.2s;
    }
    .upload-btn:hover {
        transform: scale(1.1);
    }
    </style>
    """, unsafe_allow_html=True)

if st.button("📤 Upload Your Work", key="upload_icon"):
    if not st.session_state['logged_in']:
        login()
    else:
        upload_file()

st.markdown("---")
show_my_work()
