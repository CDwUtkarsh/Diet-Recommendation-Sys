import streamlit as st

# Page config
st.set_page_config(
    page_title="NutriGenie",
    page_icon="🥗",
    layout="wide"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>

.main-title {
    font-size:55px;
    font-weight:700;
    background: -webkit-linear-gradient(#2ecc71, #27ae60);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    font-size:20px;
    color:#cccccc;
}

.card {
    background-color:#111827;
    padding:25px;
    border-radius:15px;
    box-shadow:0px 4px 20px rgba(0,0,0,0.4);
}

div.stButton > button {
    background: linear-gradient(90deg,#2ecc71,#27ae60);
    color:white;
    font-size:18px;
    border-radius:10px;
    padding:12px 30px;
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown(
    "<h1 class='main-title'>🥗 NutriGenie</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='subtitle'>Your Diet Recommendation Assistant</p>",
    unsafe_allow_html=True
)

st.markdown("---")

# ---------- FEATURE CARDS ----------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
    <h3>🥗 Smart Diet Plans</h3>
    <p>Personalized diet recommendations based on your body metrics and goals.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h3>⚡ Fast AI Recommendations</h3>
    <p>Machine learning model suggests optimal food combinations instantly.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    <h3>📊 Nutrition Insights</h3>
    <p>Get calories, macros and balanced nutrition suggestions.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ---------- CTA ----------
st.markdown("### 🚀 Start generating your diet plan")

if st.button("Generate Diet Recommendation"):
    st.switch_page("pages/Diet_Recommendation.py")

# ---------- SIDEBAR ----------
st.sidebar.title("🥗 NutriGenie")
st.sidebar.markdown(
    """
    **Your Personal Diet Assistant**  
    Get personalized diet recommendations based on your body metrics and goals.  
    Powered by FastAPI, Streamlit and Scikit-Learn.
    """
)
# ---------- FOOTER ----------
st.markdown(
"""
---
Built using **FastAPI + Streamlit + Scikit-Learn**

GitHub:  
https://github.com/CDwUtkarsh/Diet-Recommendation-System
"""
)