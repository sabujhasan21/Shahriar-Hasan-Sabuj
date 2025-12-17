import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# ===============================
# Page Config
# ===============================
st.set_page_config(
    page_title="Digital ID & My Work | Shahriar",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ===============================
# Hide Streamlit UI
# ===============================
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.block-container {padding-top:0rem; padding-bottom:0rem;}
</style>
""", unsafe_allow_html=True)

# ===============================
# Sidebar Menu
# ===============================
page = st.sidebar.selectbox("Menu", ["🏠 Home / Digital ID", "📤 My Work Upload"])

# ===============================
# Session State for Login
# ===============================
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# ===============================
# Digital ID Page
# ===============================
def digital_id_page():
    html_code = """
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
    body {
        margin: 0;
        height: 100vh;
        background: linear-gradient(-45deg, #e3f2fd, #bbdefb, #e1f5fe, #cfd8dc);
        background-size: 400% 400%;
        animation: gradientBG 12s ease infinite;
        font-family: 'Segoe UI', sans-serif;
    }
    @keyframes gradientBG {0% {background-position: 0% 50%;} 50% {background-position: 100% 50%;} 100% {background-position: 0% 50%;}}

    .profile-card {
        background: white;
        width: 60%;
        margin: 120px auto;
        padding: 45px 55px;
        border-radius: 16px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.18);
        opacity: 0;
        transform: translateY(40px);
        animation: cardIn 1.2s ease forwards;
    }
    @keyframes cardIn { to {opacity:1; transform:translateY(0);} }
    .profile-card:hover {transform: translateY(-6px) scale(1.01); box-shadow:0 20px 45px rgba(0,0,0,0.25); transition: all 0.3s ease;}
    .name {font-size:34px; font-weight:bold; color:#0b2545; border-right:3px solid #0b2545; width: fit-content; white-space: nowrap; overflow: hidden; animation: typing 2.8s steps(30), blink 0.7s infinite;}
    @keyframes typing {from{width:0;} to{width:100%;}}
    @keyframes blink {50%{border-color:transparent;}}
    .designation {font-size:18px; color:#000000; margin:10px 0 25px; opacity:0; animation: fadeIn 1s ease forwards; animation-delay:2.8s;}
    .line {height:2px; background:#0b2545; width:0; animation: lineGrow 1s ease forwards; animation-delay:3.2s;}
    @keyframes lineGrow {to{width:100%;}}
    .info p {font-size:18px; line-height:2; opacity:0; transform: translateX(-20px); animation: infoIn 0.8s ease forwards;}
    .info p:nth-child(1){animation-delay:3.8s;}
    .info p:nth-child(2){animation-delay:4.2s;}
    @keyframes infoIn {to{opacity:1; transform:translateX(0);}}
    .label{font-weight:bold;color:#0b2545;}
    .social-links{margin-top:25px; opacity:0; animation:infoIn 0.8s ease forwards; animation-delay:4.5s;}
    .social-links a{ text-decoration:none; color:#0b2545; margin-right:20px; font-size:22px; transition: color 0.3s;}
    .social-links a:hover{color:#1976d2;}
    @media(max-width:768px){.profile-card{width:90%;margin:60px auto;padding:30px;}.name{font-size:28px;}}
    </style>
    <script>
    function goFullScreen() {const elem=document.documentElement;if(elem.requestFullscreen) elem.requestFullscreen();}
    window.onload = ()=>setTimeout(goFullScreen,600);
    </script>
    </head>
    <body>
    <div class="profile-card">
        <div class="name">Md Shahriar Hasan Sabuj</div>
        <div class="designation">Assistant Officer (Student Affairs)</div>
        <div class="line"></div>
        <div class="info">
            <p><span class="label">Email:</span> info.dusc@daffodilvarsity.edu.bd</p>
            <p><span class="label">Phone:</span> 01400808455</p>
        </div>
        <div class="social-links">
            <a href="https://www.facebook.com/sabuj22" target="_blank"><i class="fab fa-facebook-square"></i></a>
            <a href="https://www.linkedin.com/" target="_blank"><i class="fab fa-linkedin"></i></a>
        </div>
    </div>
    </body>
    </html>
    """
    components.html(html_code, height=800, scrolling=False)

# ===============================
# My Work Upload Page
# ===============================
UPLOAD_DIR = Path("my_work_uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

def login_form():
    st.subheader("Login to Upload")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "sabuj2025" and password == "sabuj":
            st.success("Login Successful! ✅")
            st.session_state['logged_in'] = True
        else:
            st.error("Invalid Username or Password ❌")

def upload_file():
    st.subheader("Upload Your Work")
    uploaded_file = st.file_uploader("Choose a file", type=["png","jpg","jpeg","pdf","txt"])
    if uploaded_file is not None:
        save_path = UPLOAD_DIR / uploaded_file.name
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"Uploaded: {uploaded_file.name} ✅")
        st.balloons()

def show_my_work():
    st.subheader("My Work Gallery")
    files = list(UPLOAD_DIR.iterdir())
    if not files:
        st.info("No work uploaded yet.")
        return
    for file in files:
        if file.suffix.lower() in [".png",".jpg",".jpeg"]:
            st.image(str(file), width=200)
        else:
            st.write(f"- {file.name}")

def my_work_page():
    if not st.session_state['logged_in']:
        login_form()
    else:
        upload_file()
    st.markdown("---")
    show_my_work()

# ===============================
# Render Pages
# ===============================
if page == "🏠 Home / Digital ID":
    digital_id_page()
else:
    my_work_page()
