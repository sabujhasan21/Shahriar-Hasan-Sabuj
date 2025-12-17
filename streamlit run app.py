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
    background: linear-gradient(135deg, #e3f2fd, #bbdefb);
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

/* Card */
.profile-card {
    background: white;
    padding: 40px 60px;
    border-radius: 16px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.2);
    text-align: left;
    opacity: 0;
    transform: translateY(50px);
    animation: fadeInUp 1.2s forwards;
    max-width: 700px;
    width: 90%;
}

/* Name typing effect */
.name {
    font-size:32px;
    font-weight:bold;
    color:#0b2545;
    border-right:3px solid #0b2545;
    width:0;
    white-space: nowrap;
    overflow: hidden;
    animation: typing 2s steps(40) forwards, blink 0.7s infinite step-end;
}

/* Designation slide-up */
.designation {
    font-size:18px;
    color:black;
    margin:10px 0 20px;
    opacity:0;
    transform: translateY(20px);
    animation: slideUp 1s forwards;
    animation-delay:2.2s;
}

/* Info fade-in */
.info {
    font-size:16px;
    color:#555;
    opacity:0;
    animation: fadeIn 1s forwards;
    animation-delay:2.8s;
    line-height:1.8;
}

/* Social links fade-in */
.social-links {
    margin-top:20px;
    opacity:0;
    animation: fadeIn 1s forwards;
    animation-delay:3.2s;
}
.social-links a {
    text-decoration:none;
    color:#0b2545;
    margin-right:10px;
    font-size:22px;
    transition: color 0.3s;
}
.social-links a:hover {color:#1976d2; cursor:pointer;}

/* Popup modal */
#popup {
    display:none;
    position:fixed;
    top:0; left:0;
    width:100%; height:100%;
    background: rgba(0,0,0,0.6);
    z-index: 1000;
}
#popupContent {
    position: relative;
    width: 80%;
    height: 80%;
    margin: 5% auto;
    background: white;
    border-radius: 10px;
    overflow: hidden;
}
#popup iframe {width:100%; height:100%; border:none;}
#popup button {
    position:absolute; top:10px; right:10px;
    padding:6px 12px; background:#1976d2; color:white; border:none; border-radius:5px; cursor:pointer;
}

/* Animations */
@keyframes fadeInUp {to {opacity:1; transform:translateY(0);}}
@keyframes typing {to {width: 480px;}}
@keyframes blink {50% {border-color: transparent;}}
@keyframes slideUp {to {opacity:1; transform:translateY(0);}}
@keyframes fadeIn {to {opacity:1;}}
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
        <a onclick="openPopup('https://example.com')" ><i class="fab fa-facebook-square"></i></a>
        <a onclick="openPopup('https://example.com')" ><i class="fab fa-linkedin"></i></a>
    </div>
</div>

<!-- Popup modal -->
<div id="popup">
    <div id="popupContent">
        <button onclick="closePopup()">Close</button>
        <iframe id="popupFrame" src=""></iframe>
    </div>
</div>

<script>
function openPopup(url){
    document.getElementById('popup').style.display='block';
    document.getElementById('popupFrame').src=url;
}
function closePopup(){
    document.getElementById('popup').style.display='none';
    document.getElementById('popupFrame').src='';
}
</script>
</body>
</html>
"""

components.html(html_code, height=600, scrolling=False)
