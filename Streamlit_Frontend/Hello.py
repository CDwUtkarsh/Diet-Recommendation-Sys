import streamlit as st

st.set_page_config(
    page_title="NutriGenie",
    page_icon="🥗",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&family=Inter:wght@300;400;500;600&display=swap');

* { margin: 0; padding: 0; box-sizing: border-box; }

html, body, [data-testid="stAppViewContainer"] {
    background: #080c10 !important;
    font-family: 'Inter', sans-serif;
    color: white;
}

[data-testid="stAppViewContainer"]::before {
    content: '';
    position: fixed;
    top: -200px; left: -200px;
    width: 600px; height: 600px;
    background: radial-gradient(circle, rgba(34,197,94,0.12) 0%, transparent 70%);
    pointer-events: none;
    z-index: 0;
}

[data-testid="stAppViewContainer"]::after {
    content: '';
    position: fixed;
    bottom: -200px; right: -200px;
    width: 500px; height: 500px;
    background: radial-gradient(circle, rgba(16,185,129,0.08) 0%, transparent 70%);
    pointer-events: none;
    z-index: 0;
}

[data-testid="stSidebar"] {
    background: #0d1117 !important;
    border-right: 1px solid rgba(34,197,94,0.12) !important;
}

[data-testid="stSidebar"] * { color: rgba(255,255,255,0.7) !important; }

section[data-testid="stMain"] > div { padding-top: 0 !important; }

#MainMenu, footer, header { visibility: hidden; }
[data-testid="stDecoration"] { display: none; }

/* ── HERO ── */
.hero {
    padding: 64px 48px 32px;
    position: relative;
    z-index: 1;
}

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(34,197,94,0.1);
    border: 1px solid rgba(34,197,94,0.25);
    border-radius: 100px;
    padding: 6px 16px;
    font-size: 12px;
    color: #4ade80;
    letter-spacing: 1px;
    text-transform: uppercase;
    font-weight: 600;
    margin-bottom: 24px;
}

.hero-badge span { 
    width: 6px; height: 6px; 
    background: #22c55e; 
    border-radius: 50%;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.5; transform: scale(0.8); }
}

.hero-title {
    font-family: 'Nunito', sans-serif;
    font-size: 72px;
    font-weight: 900;
    line-height: 1.05;
    letter-spacing: -2px;
    margin-bottom: 20px;
    color: #ffffff;
}

.hero-title .green {
    background: linear-gradient(135deg, #22c55e, #86efac);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-sub {
    font-size: 18px;
    color: rgba(255,255,255,0.45);
    font-weight: 400;
    max-width: 480px;
    line-height: 1.6;
    margin-bottom: 40px;
}

/* ── STATS BAR ── */
.stats-bar {
    display: flex;
    gap: 0;
    margin: 0 48px 40px;
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px;
    overflow: hidden;
    position: relative;
    z-index: 1;
}

.stat-item {
    flex: 1;
    padding: 24px 28px;
    border-right: 1px solid rgba(255,255,255,0.07);
    text-align: center;
}

.stat-item:last-child { border-right: none; }

.stat-num {
    font-family: 'Nunito', sans-serif;
    font-size: 32px;
    font-weight: 900;
    color: #22c55e;
    letter-spacing: -1px;
}

.stat-label {
    font-size: 12px;
    color: rgba(255,255,255,0.35);
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-top: 4px;
    font-weight: 500;
}

/* ── FEATURE CARDS ── */
.cards-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    margin: 0 48px 40px;
    position: relative;
    z-index: 1;
}

.card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 20px;
    padding: 28px;
    position: relative;
    overflow: hidden;
    transition: all 0.3s ease;
}

.card:hover {
    border-color: rgba(34,197,94,0.35);
    background: rgba(34,197,94,0.05);
    transform: translateY(-3px);
    box-shadow: 0 16px 48px rgba(0,0,0,0.3), 0 0 24px rgba(34,197,94,0.08);
}

.card-glow {
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(34,197,94,0.4), transparent);
}

.card-icon-wrap {
    width: 48px; height: 48px;
    border-radius: 12px;
    display: flex; align-items: center; justify-content: center;
    font-size: 22px;
    margin-bottom: 16px;
}

.icon-green { background: rgba(34,197,94,0.15); }
.icon-blue  { background: rgba(59,130,246,0.15); }
.icon-amber { background: rgba(245,158,11,0.15); }

.card-title {
    font-family: 'Nunito', sans-serif;
    font-size: 17px;
    font-weight: 800;
    color: #f8fafc;
    margin-bottom: 8px;
    letter-spacing: -0.3px;
}

.card-desc {
    font-size: 13.5px;
    color: rgba(255,255,255,0.4);
    line-height: 1.65;
}

/* ── CTA ── */
.cta-section {
    margin: 0 48px 32px;
    background: linear-gradient(135deg, rgba(34,197,94,0.1) 0%, rgba(16,185,129,0.05) 100%);
    border: 1px solid rgba(34,197,94,0.2);
    border-radius: 24px;
    padding: 40px 48px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: relative;
    z-index: 1;
    overflow: hidden;
}

.cta-section::before {
    content: '🥗';
    position: absolute;
    right: 48px; top: 50%;
    transform: translateY(-50%);
    font-size: 96px;
    opacity: 0.07;
    pointer-events: none;
}

.cta-left h2 {
    font-family: 'Nunito', sans-serif;
    font-size: 26px;
    font-weight: 900;
    color: #f8fafc;
    letter-spacing: -0.5px;
    margin-bottom: 6px;
}

.cta-left p {
    font-size: 14px;
    color: rgba(255,255,255,0.4);
}

/* ── FOOTER ── */
.footer {
    text-align: center;
    padding: 20px 48px 32px;
    color: rgba(255,255,255,0.2);
    font-size: 13px;
    position: relative;
    z-index: 1;
}

.footer a { color: rgba(34,197,94,0.6); text-decoration: none; }
.footer a:hover { color: #22c55e; }

/* ── BUTTON ── */
.stButton > button {
    background: linear-gradient(135deg, #22c55e, #16a34a) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 14px 32px !important;
    font-size: 15px !important;
    font-weight: 700 !important;
    font-family: 'Nunito', sans-serif !important;
    letter-spacing: 0.2px !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 4px 24px rgba(34,197,94,0.3) !important;
    width: auto !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 32px rgba(34,197,94,0.45) !important;
    background: linear-gradient(135deg, #16a34a, #15803d) !important;
}
</style>

<!-- HERO -->
<div class="hero">
    <div class="hero-badge"><span></span> AI-Powered Nutrition</div>
    <div class="hero-title">Meet <span class="green">NutriGenie</span><br>Your Diet Assistant</div>
    <div class="hero-sub">Personalized meal plans crafted from your body metrics — smart, fast, and tailored to your goals.</div>
</div>

<!-- STATS -->
<div class="stats-bar">
    <div class="stat-item">
        <div class="stat-num">500K+</div>
        <div class="stat-label">Recipes</div>
    </div>
    <div class="stat-item">
        <div class="stat-num">9</div>
        <div class="stat-label">Nutrition Metrics</div>
    </div>
    <div class="stat-item">
        <div class="stat-num">&lt;2s</div>
        <div class="stat-label">AI Response</div>
    </div>
    <div class="stat-item">
        <div class="stat-num">100%</div>
        <div class="stat-label">Personalized</div>
    </div>
</div>

<!-- FEATURE CARDS -->
<div class="cards-grid">
    <div class="card">
        <div class="card-glow"></div>
        <div class="card-icon-wrap icon-green">🥗</div>
        <div class="card-title">Smart Diet Plans</div>
        <div class="card-desc">Personalized recommendations based on your BMI, activity level, and fitness goals.</div>
    </div>
    <div class="card">
        <div class="card-glow"></div>
        <div class="card-icon-wrap icon-blue">⚡</div>
        <div class="card-title">Fast AI Recommendations</div>
        <div class="card-desc">Machine learning model suggests optimal food combinations instantly using cosine similarity.</div>
    </div>
    <div class="card">
        <div class="card-glow"></div>
        <div class="card-icon-wrap icon-amber">📊</div>
        <div class="card-title">Nutrition Insights</div>
        <div class="card-desc">Get calories, macros, and balanced nutrition insights for breakfast, lunch & dinner.</div>
    </div>
</div>

<!-- CTA -->
<div class="cta-section">
    <div class="cta-left">
        <h2>🚀 Ready to eat better?</h2>
        <p>Enter your details and get your personalized meal plan in seconds.</p>
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    if st.button("Generate Diet Plan →", use_container_width=True):
        st.switch_page("pages/Diet_Recommendation.py")

st.markdown("""
<div class="footer">
    Built with ❤️ using <strong>FastAPI + Streamlit + Scikit-Learn</strong> &nbsp;|&nbsp;
    <a href="https://github.com/CDwUtkarsh/Diet-Recommendation-System" target="_blank">GitHub ↗</a>
</div>
""", unsafe_allow_html=True)