import streamlit as st
from textwrap import dedent

# ===============================
# Page Config (Fullscreen)
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
.block-container { padding: 0rem; }
</style>
""", unsafe_allow_html=True)

# ===============================
# Auto Fullscreen (Kiosk Mode)
# ===============================
st.markdown("""
<script>
document.documentElement.requestFullscreen();
</script>
""", unsafe_allow_html=True)

# ===============================
# Styles
# ===============================
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #e3f2fd, #bbdefb);
    font-family: Arial, sans-serif;
}

.card {
    background: white;
    width: 420px;
    margin: 60px auto;
    padding: 35px;
    border-radius: 18px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.2);
    text-align: center;
}

.avatar {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    margin-bottom: 15px;
}

.name {
    font-size: 24px;
    font-weight: bold;
    color: #0b2545;
}

.role {
    font-size: 15px;
    color: #555;
    margin-bottom: 20px;
}

.info {
    text-align: left;
    font-size: 15px;
    line-height: 1.8;
}

.label {
    font-weight: bold;
    color: #0b2545;
}

.btn {
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# vCard Data
# ===============================
vcard = dedent("""
BEGIN:VCARD
VERSION:3.0
FN:Md Shahriar Hasan Sabuj
TITLE:Assistant Officer (Student Affairs)
ORG:Daffodil University School & College
TEL:01400808455
EMAIL:info.dusc@daffodilvarsity.edu.bd
END:VCARD
""")

# ===============================
# CV Placeholder
# ===============================
cv_text = dedent("""
Md Shahriar Hasan Sabuj
Assistant Officer (Student Affairs)

Organization:
Daffodil University School & College

Email: info.dusc@daffodilvarsity.edu.bd
Phone: 01400808455
""")

# ===============================
# UI Card
# ===============================
st.markdown("""
<div class="card">
    <img class="avatar" src="https://i.imgur.com/6VBx3io.png">
    <div class="name">Md Shahriar Hasan Sabuj</div>
    <div class="role">Assistant Officer (Student Affairs)</div>

    <div class="info">
        <p><span class="label">Email:</span> info.dusc@daffodilvarsity.edu.bd</p>
        <p><span class="label">Phone:</span> 01400808455</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ===============================
# Download Buttons
# ===============================
col1, col2 = st.columns(2)

with col1:
    st.download_button(
        "📇 Download vCard",
        vcard,
        file_name="Shahriar_Sabuj.vcf",
        mime="text/vcard"
    )

with col2:
    st.download_button(
        "📄 Download CV",
        cv_text,
        file_name="Shahriar_Sabuj_CV.txt",
        mime="text/plain"
    )
