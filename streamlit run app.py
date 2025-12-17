import streamlit as st
import base64

# Page config (FULL SCREEN)
st.set_page_config(
    page_title="Profile | Md Shahriar Hasan Sabuj",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit default UI
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding: 0rem;
        }
    </style>
""", unsafe_allow_html=True)

# Load background image
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

bg_image = get_base64_image("background.png")  # image name

# Custom UI
st.markdown(f"""
<style>
body {{
    background-image: url("data:image/png;base64,{bg_image}");
    background-size: cover;
    background-position: center;
}}

.profile-card {{
    background: white;
    width: 60%;
    margin: 120px auto;
    padding: 40px 50px;
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    font-family: Arial, sans-serif;
}}

.name {{
    font-size: 32px;
    font-weight: bold;
    color: #0b2545;
}}

.designation {{
    font-size: 18px;
    color: #555;
    margin-bottom: 25px;
}}

.line {{
    height: 2px;
    background: #0b2545;
    width: 100%;
    margin-bottom: 25px;
}}

.info {{
    font-size: 18px;
    line-height: 2;
}}

.label {{
    font-weight: bold;
    color: #0b2545;
}}
</style>

<div class="profile-card">
    <div class="name">Md Shahriar Hasan Sabuj</div>
    <div class="designation">Assistant Officer (Student Affairs)</div>
    <div class="line"></div>

    <div class="info">
        <p><span class="label">Email:</span> info.dusc@daffodilvarsity.edu.bd</p>
        <p><span class="label">Phone:</span> 01400808455</p>
    </div>
</div>
""", unsafe_allow_html=True)
