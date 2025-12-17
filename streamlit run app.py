import streamlit as st
import streamlit.components.v1 as components

# ===============================
# Page Config
# ===============================
st.set_page_config(
    page_title="Digital ID | Md Shahriar Hasan Sabuj",
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
</style>
""", unsafe_allow_html=True)

# ===============================
# HTML + CSS + JS (With Social Links)
# ===============================
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

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Card */
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

@keyframes cardIn {
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.profile-card:hover {
    transform: translateY(-6px) scale(1.01);
    box-shadow: 0 20px 45px rgba(0,0,0,0.25);
    transition: all 0.3s ease;
}

.name {
    font-size: 34px;
    font-weight: bold;
    color: #0b2545;
    border-right: 3px solid #0b2545;
    width: fit-content;
    white-space: nowrap;
    overflow: hidden;
    animation: typing 2.8s steps(30), blink 0.7s infinite;
}

@keyframes typing { from {width: 0;} to {width: 100%;} }
@keyframes blink { 50% {border-color: transparent;} }

.designation {
    font-size: 18px;
    color: #555;
    margin: 20px 0 25px;
    opacity: 0;
    animation: fadeIn 1s ease forwards;
    animation-delay: 2.8s;
}

.line {
    height: 2px;
    background: #0b2545;
    width: 0;
    animation: lineGrow 1s ease forwards;
    animation-delay: 3.2s;
}

@keyframes lineGrow { to {width: 100%;} }

.info p {
    font-size: 18px;
    line-height: 2;
    opacity: 0;
    transform: translateX(-20px);
    animation: infoIn 0.8s ease forwards;
}
.info p:nth-child(1) {animation-delay: 3.8s;}
.info p:nth-child(2) {animation-delay: 4.2s;}

@keyframes infoIn {
    to {opacity:1; transform:translateX(0);}
}

.label { font-weight: bold; color: #0b2545; }

/* Social links */
.social-links {
    margin-top: 25px;
    opacity: 0;
    animation: infoIn 0.8s ease forwards;
    animation-delay: 4.5s;
}
.social-links a {
    text-decoration: none;
    color: #0b2545;
    margin-right: 20px;
    font-size: 22px;
    transition: color 0.3s;
}
.social-links a:hover {
    color: #1976d2;
}

/* Mobile */
@media (max-width: 768px) {
    .profile-card {
        width: 90%;
        margin: 60px auto;
        padding: 30px;
    }
    .name { font-size: 28px; }
}
</style>

<script>
function goFullScreen() {
    const elem = document.documentElement;
    if (elem.requestFullscreen) elem.requestFullscreen();
}
window.onload = () => setTimeout(goFullScreen, 600);
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

    <!-- Social Links -->
    <div class="social-links">
        <a href="https://www.facebook.com/sabuj22" target="_blank"><i class="fab fa-facebook-square"></i></a>
        <a href="https://www.linkedin.com/" target="_blank"><i class="fab fa-linkedin"></i></a>
    </div>
</div>

</body>
</html>
"""

# Render
components.html(html_code, height=800, scrolling=False)
