import streamlit as st
import pandas as pd
from utils.Generate_Recommendations import Generator
from random import uniform as rnd
from ImageFinder.ImageFinder import get_images_links as find_image
from streamlit_echarts import st_echarts

st.set_page_config(page_title="Automatic Diet Recommendation", page_icon="💪", layout="wide")

# ── RESPONSIVE CSS ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&family=Inter:wght@300;400;500;600&display=swap');

*, *::before, *::after { box-sizing: border-box; }

html, body, [data-testid="stAppViewContainer"] {
    background: #080c10 !important;
    font-family: 'Inter', sans-serif !important;
    color: #e2e8f0 !important;
}
[data-testid="stSidebar"] {
    background: #0d1117 !important;
    border-right: 1px solid rgba(34,197,94,0.12) !important;
}
[data-testid="stSidebar"] * { color: rgba(255,255,255,0.65) !important; }
section[data-testid="stMain"] > div { padding-top: 0 !important; }
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stDecoration"] { display: none; }

/* ── PAGE HEADER ── */
.page-header {
    padding: clamp(20px, 4vw, 36px) clamp(16px, 4vw, 48px) clamp(16px, 3vw, 28px);
    border-bottom: 1px solid rgba(255,255,255,0.06);
    background: linear-gradient(135deg, rgba(34,197,94,0.06) 0%, transparent 60%);
}
.page-header h1 {
    font-family: 'Nunito', sans-serif;
    font-size: clamp(22px, 5vw, 38px);
    font-weight: 900;
    letter-spacing: -1.5px; color: #f8fafc; margin: 0;
}
.page-header p {
    color: rgba(255,255,255,0.4) !important;
    font-size: clamp(12px, 2vw, 14px);
    margin-top: 6px;
}

/* ── NUMBER INPUT — force dark bg + white text ── */
input[type="number"],
input[type="text"],
[data-testid="stNumberInput"] input {
    background-color: #1e2433 !important;
    color: #ffffff !important;
    border: 1px solid rgba(255,255,255,0.18) !important;
    border-radius: 8px !important;
    font-size: 15px !important;
    font-weight: 600 !important;
    -webkit-text-fill-color: #ffffff !important;
    caret-color: #22c55e !important;
    width: 100% !important;
}
input[type="number"]:focus,
[data-testid="stNumberInput"] input:focus {
    border-color: #22c55e !important;
    box-shadow: 0 0 0 2px rgba(34,197,94,0.2) !important;
    outline: none !important;
}

/* ── SELECT BOX ── */
div[data-baseweb="select"] > div {
    background-color: #1a2030 !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 10px !important;
    color: #ffffff !important;
    min-height: 42px !important;
}
div[data-baseweb="select"] > div:focus-within {
    border-color: rgba(34,197,94,0.5) !important;
    box-shadow: 0 0 0 2px rgba(34,197,94,0.12) !important;
}
div[data-baseweb="select"] span {
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
}
div[data-baseweb="select"] input {
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
    background: transparent !important;
}
div[data-baseweb="select"] svg { fill: rgba(255,255,255,0.55) !important; }

/* ── SELECTBOX DROPDOWN FIX ── */
div[data-baseweb="popover"] {
    background: #111520 !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 10px !important;
}
div[data-baseweb="menu"] {
    background: #111520 !important;
}
div[data-baseweb="menu"] li {
    background: transparent !important;
    color: rgba(255,255,255,0.85) !important;
    font-size: 14px !important;
}
div[data-baseweb="menu"] li:hover {
    background: rgba(34,197,94,0.12) !important;
    color: #22c55e !important;
}
div[data-baseweb="menu"] li[aria-selected="true"] {
    background: rgba(34,197,94,0.15) !important;
    color: #22c55e !important;
}

/* ── LABELS ── */
label[data-testid="stWidgetLabel"] p,
label[data-testid="stWidgetLabel"] {
    color: rgba(255,255,255,0.6) !important;
    font-size: 13px !important; font-weight: 500 !important;
}

/* ── RADIO ── */
[data-testid="stRadio"] label p,
[data-testid="stRadio"] div[data-testid="stMarkdownContainer"] p {
    color: rgba(255,255,255,0.75) !important;
}

/* ── SELECT SLIDER ── */
[data-testid="stSlider"] {
    padding-bottom: 4px !important;
}
[data-testid="stSlider"] [role="slider"] {
    background-color: #22c55e !important;
    border-color: #22c55e !important;
}
[data-testid="stSlider"] [data-testid="stMarkdownContainer"] p {
    color: #22c55e !important; font-weight: 700 !important; font-size: 13px !important;
}
[data-testid="stSlider"] [class*="StyledThumbValue"],
[data-testid="stSlider"] small {
    color: rgba(255,255,255,0.35) !important;
    font-size: 10px !important;
}
[data-testid="stSlider"] [data-baseweb="slider"] [role="slider"] {
    background: #22c55e !important; border-color: #22c55e !important;
}

/* ── SUBMIT BUTTON ── */
[data-testid="stFormSubmitButton"] > button {
    background: linear-gradient(135deg, #22c55e, #16a34a) !important;
    color: #ffffff !important; -webkit-text-fill-color: #ffffff !important;
    border: none !important; border-radius: 12px !important;
    padding: 14px 28px !important; font-size: 15px !important;
    font-weight: 800 !important; font-family: 'Nunito', sans-serif !important;
    box-shadow: 0 4px 20px rgba(34,197,94,0.3) !important;
    transition: all 0.2s !important;
    width: 100% !important;
}
[data-testid="stFormSubmitButton"] > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 28px rgba(34,197,94,0.45) !important;
}

/* ── EXPANDER ── */
[data-testid="stExpander"] {
    background: #111824 !important;
    border: 1px solid rgba(255,255,255,0.09) !important;
    border-radius: 12px !important; margin-bottom: 8px !important;
    overflow: hidden !important;
}
[data-testid="stExpander"]:hover {
    border-color: rgba(34,197,94,0.28) !important;
}
[data-testid="stExpander"] details > summary p,
[data-testid="stExpander"] details > summary span {
    color: #e2e8f0 !important;
    font-weight: 600 !important; font-size: 14px !important;
}
[data-testid="stExpander"] details > summary svg {
    fill: rgba(255,255,255,0.45) !important;
}

/* ── SUCCESS ── */
[data-testid="stAlert"] {
    background: rgba(34,197,94,0.08) !important;
    border: 1px solid rgba(34,197,94,0.2) !important;
    border-radius: 12px !important;
}
[data-testid="stAlert"] p { color: #4ade80 !important; }

/* ── SECTION HELPERS ── */
.section-title {
    font-family: 'Nunito', sans-serif;
    font-size: clamp(18px, 3vw, 22px);
    font-weight: 900; color: #f8fafc; letter-spacing: -0.5px;
}
.sec-div {
    height: 1px; margin: clamp(16px, 3vw, 32px) clamp(8px, 3vw, 48px) clamp(14px, 2.5vw, 28px);
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.07), transparent);
}
.form-section-label {
    font-size: 11px; font-weight: 700; color: rgba(255,255,255,0.38);
    text-transform: uppercase; letter-spacing: 2px; margin-bottom: 16px;
    display: flex; align-items: center; gap: 10px;
}
.form-section-label::after {
    content: ''; flex: 1; height: 1px; background: rgba(255,255,255,0.07);
}

/* ── BMI CARD ── */
.bmi-card {
    background: #111824; border: 1px solid rgba(255,255,255,0.09);
    border-radius: 18px; padding: clamp(14px, 2vw, 24px) clamp(14px, 2.5vw, 28px);
    position: relative; overflow: hidden; margin: 0 !important;
}
.bmi-card::before {
    content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
    background: linear-gradient(90deg, transparent, rgba(34,197,94,0.4), transparent);
}
.bmi-value {
    font-family: 'Nunito', sans-serif;
    font-size: clamp(28px, 5vw, 42px);
    font-weight: 900; letter-spacing: -2px; color: #f8fafc;
}

/* ── CALORIE CARDS ── */
.cal-card {
    background: #111824; border: 1px solid rgba(255,255,255,0.09);
    border-radius: 16px; padding: clamp(12px, 2vw, 20px) clamp(10px, 2vw, 22px);
    text-align: center; transition: border-color 0.2s;
    margin-bottom: 10px;
}
.cal-card:hover { border-color: rgba(34,197,94,0.28); }
.cal-card-label {
    font-size: clamp(10px, 1.5vw, 12px);
    color: rgba(255,255,255,0.42); text-transform: uppercase;
    letter-spacing: 1px; margin-bottom: 8px; font-weight: 600;
}
.cal-card-value {
    font-family: 'Nunito', sans-serif;
    font-size: clamp(18px, 3vw, 26px);
    font-weight: 900; color: #22c55e; letter-spacing: -1px;
}
.cal-card-delta { font-size: clamp(10px, 1.5vw, 12px); color: rgba(255,255,255,0.32); margin-top: 4px; }

/* ── MEAL BADGES ── */
.meal-badge {
    display: inline-flex; align-items: center;
    padding: 5px 14px; border-radius: 8px;
    font-size: 11px; font-weight: 700; text-transform: uppercase;
    letter-spacing: 1.5px; margin-bottom: 14px;
}
.badge-b { background: rgba(251,191,36,0.12); color: #fbbf24; border: 1px solid rgba(251,191,36,0.2); }
.badge-l { background: rgba(59,130,246,0.12);  color: #60a5fa; border: 1px solid rgba(59,130,246,0.2); }
.badge-d { background: rgba(167,139,250,0.12); color: #a78bfa; border: 1px solid rgba(167,139,250,0.2); }
.badge-s { background: rgba(251,113,133,0.12); color: #fb7185; border: 1px solid rgba(251,113,133,0.2); }

/* ── NUTRITION PILLS ── */
.nut-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 8px; margin: 10px 0 16px;
}
.nut-pill {
    background: rgba(34,197,94,0.07); border: 1px solid rgba(34,197,94,0.16);
    border-radius: 10px; padding: 10px 8px; text-align: center;
}
.nut-val { font-family: 'Nunito', sans-serif; font-size: 16px; font-weight: 800; color: #4ade80; }
.nut-key { font-size: 9px; color: rgba(255,255,255,0.4); text-transform: uppercase; letter-spacing: 0.5px; margin-top: 2px; }

/* ── CAL HERO ── */
.cal-hero {
    background: linear-gradient(135deg, rgba(34,197,94,0.1), rgba(16,185,129,0.05));
    border: 1px solid rgba(34,197,94,0.2); border-radius: 18px;
    padding: clamp(16px, 3vw, 28px) clamp(14px, 3vw, 36px);
    text-align: center; margin: 16px 0;
}
.cal-hero-label {
    font-size: clamp(10px, 1.5vw, 12px);
    color: rgba(255,255,255,0.4); text-transform: uppercase;
    letter-spacing: 2px; margin-bottom: 6px; font-weight: 600;
}
.cal-hero-val {
    font-family: 'Nunito', sans-serif;
    font-size: clamp(34px, 7vw, 52px);
    font-weight: 900; color: #22c55e; letter-spacing: -3px; line-height: 1;
}
.cal-hero-unit { font-size: clamp(14px, 2vw, 18px); color: rgba(255,255,255,0.35); font-weight: 400; }

/* ── DATAFRAME ── */
[data-testid="stDataFrame"] { border-radius: 12px !important; overflow: hidden !important; }
[data-testid="stDataFrame"] th { background: rgba(34,197,94,0.1) !important; color: rgba(255,255,255,0.7) !important; }
[data-testid="stDataFrame"] td { color: rgba(255,255,255,0.75) !important; background: #111824 !important; }

/* ── RECIPE IMAGE ── */
.recipe-img {
    width: 100%;
    max-width: 220px;
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.1);
    display: block;
    margin: 0 auto 12px;
}

/* ── RESPONSIVE: MOBILE OVERRIDES ── */
@media (max-width: 640px) {
    .page-header { padding: 20px 16px 16px; }
    .page-header h1 { font-size: 22px; letter-spacing: -0.5px; }
    .sec-div { margin: 16px 8px 14px; }
    .bmi-card { margin: 0 8px !important; }
    .nut-grid { grid-template-columns: repeat(2, 1fr); }
    .cal-hero-val { font-size: 36px; }
    [data-testid="stFormSubmitButton"] > button { padding: 12px 20px !important; font-size: 14px !important; }
}

/* ── STACKED FORM WRAPPER ── */
.form-wrap {
    padding: 0 clamp(8px, 3vw, 48px);
}

/* ── ENSURE COLUMNS FLOW on narrow screens ── */
[data-testid="stHorizontalBlock"] {
    flex-wrap: wrap !important;
    gap: 8px !important;
}
[data-testid="stHorizontalBlock"] > div {
    min-width: 140px !important;
    flex: 1 1 140px !important;
}

/* Prevent horizontal overflow */
.main .block-container {
    max-width: 100% !important;
    padding-left: clamp(8px, 3vw, 48px) !important;
    padding-right: clamp(8px, 3vw, 48px) !important;
    overflow-x: hidden !important;
}
</style>
""", unsafe_allow_html=True)

# ── CONSTANTS ──────────────────────────────────────────────────────────────────
nutritions_values = ['Calories','FatContent','SaturatedFatContent','CholesterolContent',
                     'SodiumContent','CarbohydrateContent','FiberContent','SugarContent','ProteinContent']

# ── SESSION STATE ──────────────────────────────────────────────────────────────
if 'person' not in st.session_state:
    st.session_state.generated = False
    st.session_state.recommendations = None
    st.session_state.person = None
    st.session_state.weight_loss_option = None

# ── PERSON CLASS ───────────────────────────────────────────────────────────────
class Person:
    def __init__(self, age, height, weight, gender, activity, meals_calories_perc, weight_loss):
        self.age = age; self.height = height; self.weight = weight
        self.gender = gender; self.activity = activity
        self.meals_calories_perc = meals_calories_perc; self.weight_loss = weight_loss

    def calculate_bmi(self):
        return round(self.weight / ((self.height / 100) ** 2), 2)

    def display_result(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:   category, color = 'Underweight', '#f87171'
        elif bmi < 25:   category, color = 'Normal',      '#4ade80'
        elif bmi < 30:   category, color = 'Overweight',  '#fbbf24'
        else:            category, color = 'Obesity',     '#f87171'
        return f'{bmi} kg/m²', category, color

    def calculate_bmr(self):
        if self.gender == 'Male':
            return 10*self.weight + 6.25*self.height - 5*self.age + 5
        return 10*self.weight + 6.25*self.height - 5*self.age - 161

    def calories_calculator(self):
        activites = ['Little/no exercise','Light exercise','Moderate exercise (3-5 days/wk)',
                     'Very active (6-7 days/wk)','Extra active (very active & physical job)']
        weights = [1.2, 1.375, 1.55, 1.725, 1.9]
        return self.calculate_bmr() * weights[activites.index(self.activity)]

    def generate_recommendations(self):
        total_calories = self.weight_loss * self.calories_calculator()
        recommendations = []
        for meal in self.meals_calories_perc:
            meal_calories = self.meals_calories_perc[meal] * total_calories
            if meal == 'breakfast':
                rn = [meal_calories,rnd(10,30),rnd(0,4),rnd(0,30),rnd(0,400),rnd(40,75),rnd(4,10),rnd(0,10),rnd(30,100)]
            elif meal == 'launch':
                rn = [meal_calories,rnd(20,40),rnd(0,4),rnd(0,30),rnd(0,400),rnd(40,75),rnd(4,20),rnd(0,10),rnd(50,175)]
            elif meal == 'dinner':
                rn = [meal_calories,rnd(20,40),rnd(0,4),rnd(0,30),rnd(0,400),rnd(40,75),rnd(4,20),rnd(0,10),rnd(50,175)]
            else:
                rn = [meal_calories,rnd(10,30),rnd(0,4),rnd(0,30),rnd(0,400),rnd(40,75),rnd(4,10),rnd(0,10),rnd(30,100)]
            generator = Generator(rn)
            recommended_recipes = generator.generate()['output']
            recommendations.append(recommended_recipes)
        for rec in recommendations:
            for recipe in rec:
                recipe['image_link'] = find_image(recipe['Name'])
        return recommendations


# ── DISPLAY CLASS ──────────────────────────────────────────────────────────────
class Display:
    def __init__(self):
        self.plans   = ["Maintain weight","Mild weight loss","Weight loss","Extreme weight loss"]
        self.weights = [1, 0.9, 0.8, 0.6]
        self.losses  = ['-0 kg/week','-0.25 kg/week','-0.5 kg/week','-1 kg/week']

    def display_bmi(self, person):
        bmi_string, category, color = person.display_result()
        st.markdown('<div class="sec-div"></div>', unsafe_allow_html=True)
        st.markdown(
            '<div style="margin:0 0 20px;">'
            '<span class="section-title">📊 BMI Calculator</span><br>'
            '<span style="font-size:13px;color:rgba(255,255,255,0.38);">Your Body Mass Index based on height & weight</span>'
            '</div>',
            unsafe_allow_html=True
        )
        # ── Responsive: stack on mobile, side-by-side on wider screens ──
        col_bmi, col_info = st.columns([1, 2])
        with col_bmi:
            st.markdown(f"""
            <div class="bmi-card">
                <div style="font-size:11px;color:rgba(255,255,255,0.38);text-transform:uppercase;letter-spacing:1.5px;margin-bottom:8px;font-weight:600;">Body Mass Index</div>
                <div class="bmi-value">{bmi_string.split()[0]} <span style="font-size:16px;color:rgba(255,255,255,0.4);font-weight:400;">kg/m²</span></div>
                <div style="margin-top:12px;display:inline-block;padding:5px 14px;border-radius:8px;
                            background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);
                            font-size:15px;font-weight:700;color:{color};">{category}</div>
            </div>""", unsafe_allow_html=True)
        with col_info:
            st.markdown("""
            <div style="padding:8px 0;font-size:14px;line-height:2.2;">
                <div style="color:rgba(255,255,255,0.75);font-weight:700;font-family:'Nunito',sans-serif;font-size:15px;margin-bottom:6px;">BMI Categories</div>
                <div style="color:rgba(255,255,255,0.5);">🔴 &nbsp;<strong style="color:rgba(255,255,255,0.72);">Underweight</strong> — Below 18.5</div>
                <div style="color:rgba(255,255,255,0.5);">🟢 &nbsp;<strong style="color:rgba(255,255,255,0.72);">Normal</strong> — 18.5 – 24.9</div>
                <div style="color:rgba(255,255,255,0.5);">🟡 &nbsp;<strong style="color:rgba(255,255,255,0.72);">Overweight</strong> — 25 – 29.9</div>
                <div style="color:rgba(255,255,255,0.5);">🔴 &nbsp;<strong style="color:rgba(255,255,255,0.72);">Obese</strong> — 30 and above</div>
                <div style="margin-top:6px;font-size:12px;color:rgba(255,255,255,0.28);">Healthy BMI range: 18.5 – 25 kg/m²</div>
            </div>""", unsafe_allow_html=True)

    def display_calories(self, person):
        maintain_calories = person.calories_calculator()
        st.markdown('<div class="sec-div"></div>', unsafe_allow_html=True)
        st.markdown(
            '<div style="margin:0 0 20px;">'
            '<span class="section-title">🔥 Calories Calculator</span><br>'
            '<span style="font-size:13px;color:rgba(255,255,255,0.38);">Daily calorie estimates based on your activity level and goal</span>'
            '</div>',
            unsafe_allow_html=True
        )
        # ── 4 cards: 2×2 on mobile, 4 across on desktop ──
        cols = st.columns(4)
        for plan, weight, loss, col in zip(self.plans, self.weights, self.losses, cols):
            with col:
                st.markdown(f"""
                <div class="cal-card">
                    <div class="cal-card-label">{plan}</div>
                    <div class="cal-card-value">{round(maintain_calories * weight)}</div>
                    <div class="cal-card-delta">Calories/day · {loss}</div>
                </div>""", unsafe_allow_html=True)

    def display_recommendation(self, person, recommendations):
        st.markdown('<div class="sec-div"></div>', unsafe_allow_html=True)
        st.markdown(
            '<div style="margin:0 0 20px;">'
            '<span class="section-title">🥗 Recommended Recipes</span><br>'
            '<span style="font-size:13px;color:rgba(255,255,255,0.38);">Top 5 personalized recipes for each meal</span>'
            '</div>',
            unsafe_allow_html=True
        )

        meals = person.meals_calories_perc
        badge_map = {
            'breakfast':'badge-b','lunch':'badge-l','dinner':'badge-d',
            'morning snack':'badge-s','afternoon snack':'badge-s','launch':'badge-l'
        }

        meal_count = len(meals)
        # ── Responsive column strategy: max 3 on tablet, stack on mobile ──
        # For 3 meals → 3 cols; for 4+ meals → 2 cols per row to avoid squishing
        if meal_count <= 3:
            columns = st.columns(meal_count)
        else:
            columns = st.columns(min(meal_count, 3))

        meal_items = list(zip(meals, recommendations))

        # If more meals than columns, we render in groups
        for idx, (meal_name, recommendation) in enumerate(meal_items):
            # Wrap to next "row" if needed
            col_idx = idx % len(columns)
            if meal_count > 3 and col_idx == 0 and idx > 0:
                columns = st.columns(min(meal_count - idx, 3))

            with columns[col_idx]:
                bc = badge_map.get(meal_name, 'badge-s')
                st.markdown(f'<div class="meal-badge {bc}">{meal_name}</div>', unsafe_allow_html=True)
                for recipe in recommendation:
                    with st.expander(recipe['Name']):
                        if recipe.get('image_link'):
                            st.markdown(
                                f'<img src="{recipe["image_link"]}" class="recipe-img" alt="{recipe["Name"]}">',
                                unsafe_allow_html=True
                            )

                        st.markdown(f"""
                        <div class="nut-grid">
                            <div class="nut-pill"><div class="nut-val">{recipe['Calories']:.0f}</div><div class="nut-key">Calories</div></div>
                            <div class="nut-pill"><div class="nut-val">{recipe['ProteinContent']:.1f}g</div><div class="nut-key">Protein</div></div>
                            <div class="nut-pill"><div class="nut-val">{recipe['CarbohydrateContent']:.1f}g</div><div class="nut-key">Carbs</div></div>
                            <div class="nut-pill"><div class="nut-val">{recipe['FatContent']:.1f}g</div><div class="nut-key">Fat</div></div>
                            <div class="nut-pill"><div class="nut-val">{recipe['FiberContent']:.1f}g</div><div class="nut-key">Fiber</div></div>
                            <div class="nut-pill"><div class="nut-val">{recipe['SodiumContent']:.0f}mg</div><div class="nut-key">Sodium</div></div>
                        </div>""", unsafe_allow_html=True)

                        st.markdown('<p style="text-align:center;color:rgba(255,255,255,0.4);font-size:12px;margin:4px 0 6px;">Nutritional Values (g)</p>', unsafe_allow_html=True)
                        nutritions_df = pd.DataFrame({v: [recipe[v]] for v in nutritions_values})
                        st.dataframe(nutritions_df, use_container_width=True, hide_index=True)

                        st.markdown('<p style="font-weight:700;font-size:13px;color:rgba(255,255,255,0.65);margin:12px 0 6px;">🛒 Ingredients</p>', unsafe_allow_html=True)
                        ingredients = recipe["RecipeIngredientParts"]
                        if isinstance(ingredients, str):
                            ingredients = ingredients.replace("c(","").replace(")","").replace('"',"")
                            ingredients = [i.strip() for i in ingredients.split(",")]
                        for ing in ingredients:
                            st.markdown(f"- {ing}")

                        st.markdown('<p style="font-weight:700;font-size:13px;color:rgba(255,255,255,0.65);margin:12px 0 6px;">📝 Recipe Instructions</p>', unsafe_allow_html=True)
                        instructions = recipe["RecipeInstructions"]
                        if isinstance(instructions, str):
                            instructions = instructions.replace("c(","").replace(")","").replace('"',"")
                            instructions = [i.strip() for i in instructions.split(",")]
                        for ins in instructions:
                            st.markdown(f"- {ins}")

                        st.markdown('<p style="font-weight:700;font-size:13px;color:rgba(255,255,255,0.65);margin:12px 0 6px;">⏱️ Cooking Time</p>', unsafe_allow_html=True)
                        st.markdown(f"""
- Cook Time : **{recipe['CookTime']}**
- Preparation Time : **{recipe['PrepTime']}**
- Total Time : **{recipe['TotalTime']}**
""")

    def display_meal_choices(self, person, recommendations):
        st.markdown('<div class="sec-div"></div>', unsafe_allow_html=True)
        st.markdown(
            '<div style="margin:0 0 20px;">'
            '<span class="section-title">🎯 Choose Your Meal Composition</span><br>'
            '<span style="font-size:13px;color:rgba(255,255,255,0.38);">Select your preferred recipe for each meal</span>'
            '</div>',
            unsafe_allow_html=True
        )

        # ── Responsive selectboxes: 1 per row on mobile, multi-col on desktop ──
        if len(recommendations) == 3:
            c1, c2, c3 = st.columns([1, 1, 1])
            with c1: b = st.selectbox('Choose your breakfast:',  [r['Name'] for r in recommendations[0]])
            with c2: l = st.selectbox('Choose your launch:',     [r['Name'] for r in recommendations[1]])
            with c3: d = st.selectbox('Choose your dinner:',     [r['Name'] for r in recommendations[2]])
            choices = [b, l, d]
        elif len(recommendations) == 4:
            c1, c2 = st.columns(2)
            with c1: b  = st.selectbox('Choose your breakfast:',     [r['Name'] for r in recommendations[0]])
            with c2: ms = st.selectbox('Choose your morning snack:', [r['Name'] for r in recommendations[1]])
            c3, c4 = st.columns(2)
            with c3: l  = st.selectbox('Choose your launch:',        [r['Name'] for r in recommendations[2]])
            with c4: d  = st.selectbox('Choose your dinner:',        [r['Name'] for r in recommendations[3]])
            choices = [b, ms, l, d]
        else:
            c1, c2, c3 = st.columns(3)
            with c1: b  = st.selectbox('Choose your breakfast:',     [r['Name'] for r in recommendations[0]])
            with c2: ms = st.selectbox('Choose your morning snack:', [r['Name'] for r in recommendations[1]])
            with c3: l  = st.selectbox('Choose your launch:',        [r['Name'] for r in recommendations[2]])
            c4, c5 = st.columns(2)
            with c4: af = st.selectbox('Choose your afternoon:',     [r['Name'] for r in recommendations[3]])
            with c5: d  = st.selectbox('Choose your dinner:',        [r['Name'] for r in recommendations[4]])
            choices = [b, ms, l, af, d]

        total_nutrition_values = {n: 0 for n in nutritions_values}
        for choice, meals_ in zip(choices, recommendations):
            for meal in meals_:
                if meal['Name'] == choice:
                    for n in nutritions_values:
                        total_nutrition_values[n] += meal[n]

        total_calories_chose = total_nutrition_values['Calories']
        loss_calories_chose  = round(person.calories_calculator() * person.weight_loss)

        st.markdown(f"""
        <div class="cal-hero">
            <div class="cal-hero-label">Total Calories Selected</div>
            <div class="cal-hero-val">{total_calories_chose:.0f} <span class="cal-hero-unit">kcal</span></div>
        </div>""", unsafe_allow_html=True)

        # ── Charts: smaller height on mobile via viewport-aware sizing ──
        st.markdown(f'<p style="text-align:center;color:rgba(255,255,255,0.45);margin:20px 0 8px;">Total Calories vs {st.session_state.weight_loss_option} Target</p>', unsafe_allow_html=True)

        # Bar chart – reduced base height for tighter mobile fit
        st_echarts(options={
            "backgroundColor": "transparent",
            "grid": {"containLabel": True, "left": "3%", "right": "3%", "bottom": "5%"},
            "xAxis": {
                "type": "category",
                "data": ['Your Selection', f"{st.session_state.weight_loss_option}"],
                "axisLabel": {"color": "rgba(255,255,255,0.5)", "fontSize": 12},
                "axisLine": {"lineStyle": {"color": "rgba(255,255,255,0.1)"}}
            },
            "yAxis": {
                "type": "value",
                "axisLabel": {"color": "rgba(255,255,255,0.5)", "fontSize": 11},
                "splitLine": {"lineStyle": {"color": "rgba(255,255,255,0.06)"}}
            },
            "series": [{
                "data": [
                    {"value": total_calories_chose, "itemStyle": {"color": ["#22c55e","#f87171"][total_calories_chose > loss_calories_chose], "borderRadius": [8,8,0,0]}},
                    {"value": loss_calories_chose,  "itemStyle": {"color": "#3b82f6", "borderRadius": [8,8,0,0]}}
                ],
                "type": "bar", "barWidth": "40%"
            }],
        }, height="320px")  # reduced from 400px for better mobile fit

        st.markdown('<p style="text-align:center;color:rgba(255,255,255,0.45);margin:20px 0 8px;">Nutritional Breakdown</p>', unsafe_allow_html=True)

        # Donut chart – reduced height
        st_echarts(options={
            "backgroundColor": "transparent",
            "tooltip": {"trigger": "item"},
            "legend": {"top": "5%", "left": "center", "textStyle": {"color": "rgba(255,255,255,0.5)"}, "itemGap": 8},
            "series": [{
                "name": "Nutritional Values",
                "type": "pie",
                "radius": ["40%", "68%"],
                "center": ["50%", "55%"],
                "avoidLabelOverlap": True,
                "itemStyle": {"borderRadius": 10, "borderColor": "#080c10", "borderWidth": 3},
                "label": {"show": False, "position": "center"},
                "emphasis": {"label": {"show": True, "fontSize": "32", "fontWeight": "bold", "color": "white"}},
                "labelLine": {"show": False},
                "data": [{"value": round(total_nutrition_values[v]), "name": v} for v in total_nutrition_values]
            }],
        }, height="420px")  # reduced from 500px


# ── RENDER ─────────────────────────────────────────────────────────────────────
display = Display()

# Page Header
st.markdown("""
<div class="page-header">
    <h1>🥗 Automatic Diet Recommendation</h1>
    <p>Fill in your body metrics and get a personalized AI-powered meal plan</p>
</div>""", unsafe_allow_html=True)

# Form
st.markdown('<div class="form-section-label" style="margin-top:24px;">📋 Your Body Metrics</div>', unsafe_allow_html=True)

with st.form("recommendation_form"):
    # ── Row 1: Age, Height, Weight  ──
    col1, col2, col3 = st.columns(3)
    with col1:
        age    = st.number_input('Age',         min_value=2,  max_value=120, step=1)
    with col2:
        height = st.number_input('Height (cm)', min_value=50, max_value=300, step=1)
    with col3:
        weight = st.number_input('Weight (kg)', min_value=10, max_value=300, step=1)

    # ── Row 2: Gender + Activity ──
    col4, col5 = st.columns([1, 2])
    with col4:
        gender = st.radio('Gender', ('Male', 'Female'))
    with col5:
        activity = st.select_slider('Activity Level', options=[
            'Little/no exercise',
            'Light exercise',
            'Moderate exercise (3-5 days/wk)',
            'Very active (6-7 days/wk)',
            'Extra active (very active & physical job)'
        ])

    # ── Row 3: Plan + Meals ──
    col6, col7 = st.columns([2, 1])
    with col6:
        option = st.selectbox('Choose your weight loss plan:', display.plans)
        st.session_state.weight_loss_option = option
        weight_loss = display.weights[display.plans.index(option)]
    with col7:
        number_of_meals = st.slider('Meals per day', min_value=3, max_value=5, step=1, value=3)

    if number_of_meals == 3:
        meals_calories_perc = {'breakfast': 0.35, 'launch': 0.40, 'dinner': 0.25}
    elif number_of_meals == 4:
        meals_calories_perc = {'breakfast': 0.30, 'morning snack': 0.05, 'launch': 0.40, 'dinner': 0.25}
    else:
        meals_calories_perc = {'breakfast': 0.30, 'morning snack': 0.05, 'launch': 0.40, 'afternoon snack': 0.05, 'dinner': 0.20}

    generated = st.form_submit_button("⚡ Generate My Diet Plan")

if generated:
    st.session_state.generated = True
    person = Person(age, height, weight, gender, activity, meals_calories_perc, weight_loss)
    with st.container():
        display.display_bmi(person)
    with st.container():
        display.display_calories(person)
    with st.spinner('🤖 Generating your personalized meal plan...'):
        recommendations = person.generate_recommendations()
        st.session_state.recommendations = recommendations
        st.session_state.person = person

if st.session_state.generated:
    with st.container():
        display.display_recommendation(st.session_state.person, st.session_state.recommendations)
        st.success('✅ Recommendation Generated Successfully!')
    with st.container():
        display.display_meal_choices(st.session_state.person, st.session_state.recommendations)