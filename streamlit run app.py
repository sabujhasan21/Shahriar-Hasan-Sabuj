import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Digital ID | Md Shahriar Hasan Sabuj",
    layout="wide"
)

# Hide Streamlit UI
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.block-container {padding-top:0rem; padding-bottom:0rem;}
</style>
""", unsafe_allow_html=True)

html_code = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
body {
    margin:0;
    font-family: Arial, sans-serif;
    background: #e3f2fd;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

.profile-card {
    background: white;
    padding: 40px 50px;
    border-radius: 16px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    text-align: center;
}

.name { font-size:32px; font-weight:bold; color:#0b2545; margin-bottom:10px; }
.designation { font-size:18px; color:black; margin-bottom:20px; }
.info { font-size:16px; line-height:1.8; color:#555; }
.social-links a { text-decoration:none; color:#0b2545; margin:0 10px; font-size:22px; transition: color 0.3s; }
.social-links a:hover { color:#1976d2; }
</style>
</head>
<body>
<div class="profile-card">
    <div class="name">Md Shahriar Hasan Sabuj</div>
    <div class="designation">Assistant Officer (Student Affairs)</div>
    <div class="info">
        <p>Email: info.dusc@daffodilvarsity.edu.bd</p>
        <p>Phone: 01400808455</p>
    </div>
    <div class="social-links">
        <a href="https://www.facebook.com/sabuj22" target="_blank"><i class="fab fa-facebook-square"></i></a>
        <a href="https://www.linkedin.com/" target="_blank"><i class="fab fa-linkedin"></i></a>
    </div>
</div>
</body>
</html>
"""

components.html(html_code, height=500, scrolling=False)
