import streamlit as st
import streamlit.components.v1 as components

# ===============================
# Page Configuration
# ===============================
st.set_page_config(
    page_title="Profile | Md Shahriar Hasan Sabuj",
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
# HTML + CSS (SAFE RENDER)
# ===============================
html_code = """
<!DOCTYPE html>
<html>
<head>
<style>
body {
    margin: 0;
    background: linear-gradient(135deg, #e3f2fd, #bbdefb);
    font-family: Arial, sans-serif;
}

.profile-card {
    background: white;
    width: 60%;
    margin: 120px auto;
    padding: 45px 55px;
    border-radius: 14px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.18);
}

.name {
    font-size: 32px;
    font-weight: bold;
    color: #0b2545;
}

.designation {
    font-size: 18px;
    color: #555;
    margin-bottom: 25px;
}

.line {
    height: 2px;
    background: #0b2545;
    width: 100%;
    margin-bottom: 25px;
}

.info {
    font-size: 18px;
    line-height: 2;
}

.label {
    font-weight: bold;
    color: #0b2545;
}

@media (max-width: 768px) {
    .profile-card {
        width: 90%;
        margin: 60px auto;
        padding: 30px;
    }
}
</style>
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
    </div>
</body>
</html>
"""

# ===============================
# Render HTML (IMPORTANT)
# ===============================
components.html(html_code, height=600, scrolling=False)
