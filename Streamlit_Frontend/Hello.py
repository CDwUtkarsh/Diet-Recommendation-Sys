import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="NutriGenie",
    page_icon="🥗",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.main-title {
    font-size:55px;
    font-weight:700;
    background: linear-gradient(90deg,#2ecc71,#27ae60);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    font-size:20px;
    color:#9ca3af;
}

.card {
    background:#111827;
    padding:30px;
    border-radius:15px;
    box-shadow:0px 6px 25px rgba(0,0,0,0.4);
    color:white;
    transition:0.3s;
}

.card:hover {
    transform:translateY(-6px);
    box-shadow:0px 10px 30px rgba(0,0,0,0.6);
}

.card h3{
    color:white;
}

.card p{
    color:#cbd5f5;
}

.center-btn{
    display:flex;
    justify-content:center;
}

div.stButton > button {
    background: linear-gradient(90deg,#2ecc71,#27ae60);
    color:white;
    font-size:18px;
    border-radius:10px;
    padding:12px 35px;
    border:none;
}

div.stButton > button:hover{
    background: linear-gradient(90deg,#27ae60,#2ecc71);
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<h1 class='main-title'>🥗 NutriGenie</h1>", unsafe_allow_html=True)

st.markdown(
    "<p class='subtitle'>Your AI powered diet recommendation assistant</p>",
    unsafe_allow_html=True
)

st.markdown("---")

# ---------------- FEATURE CARDS ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
    <h3>🥗 Smart Diet Plans</h3>
    <p>Personalized diet recommendations based on your body metrics and fitness goals.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h3>⚡ Fast AI Recommendations</h3>
    <p>Machine learning algorithm suggests optimal food combinations instantly.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    <h3>📊 Nutrition Insights</h3>
    <p>Get calorie, macro and balanced nutrition insights for a healthier lifestyle.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ---------------- CTA ----------------
st.markdown("### 🚀 Start generating your diet plan")

col1, col2, col3 = st.columns([1,2,1])

with col2:
    if st.button("Generate Diet Recommendation"):
        st.switch_page("pages/Diet_Recommendation.py")

# ---------------- SIDEBAR ----------------
st.sidebar.title("🥗 NutriGenie")

st.sidebar.markdown("""
### Your Personal Diet Assistant

Get **personalized diet recommendations** based on your:

- Age
- Height
- Weight
- Activity Level
- Fitness Goal

⚡ Powered by **FastAPI + Streamlit + Scikit-Learn**
""")

# ---------------- FOOTER ----------------
st.markdown("""
---
<center>

Built with ❤️ using **FastAPI + Streamlit + Scikit-Learn**

GitHub:  
https://github.com/CDwUtkarsh/Diet-Recommendation-System

</center>
""", unsafe_allow_html=True)