# 🥗 NutriGenie – AI Diet Recommendation System

**NutriGenie** is an AI-powered diet recommendation system that generates personalized meal plans based on a user's body metrics, activity level, and weight goals.

The application uses **Machine Learning, FastAPI, and Streamlit** to recommend healthy meals, visualize nutritional information, and provide recipe guidance.

---

# 🚀 Features

✅ Personalized diet recommendations
✅ BMI calculator
✅ Daily calorie requirement estimation
✅ AI-powered meal recommendations
✅ Recipe ingredients & cooking instructions
✅ Nutrition value breakdown
✅ Meal image preview
✅ Interactive nutrition charts

---

# 🧠 Tech Stack

| Technology            | Purpose                   |
| --------------------- | ------------------------- |
| **Python**            | Core programming language |
| **Streamlit**         | Frontend web interface    |
| **FastAPI**           | Backend API               |
| **Scikit-Learn**      | Recommendation model      |
| **Pandas**            | Data processing           |
| **Streamlit ECharts** | Nutrition visualization   |

---

# 🏗 System Architecture

User Input (Age, Height, Weight, Activity Level)
↓
Streamlit Frontend (User Interface)
↓
FastAPI Backend (API)
↓
Machine Learning Recommendation Model
↓
Recipe Recommendation Engine
↓
Nutrition Visualization

---

# 📂 Project Structure

```
Diet-Recommendation-System
│
├── FastAPI_Backend
│   └── main.py
│
├── Streamlit_Frontend
│   ├── Hello.py
│   ├── pages
│   │   ├── Diet_Recommendation.py
│   │   └── Custom_Food_Recommendation.py
│
├── utils
│   └── Generate_Recommendations.py
│
├── ImageFinder
│   └── ImageFinder.py
│
├── Data
│   └── dataset.csv
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```
git clone https://github.com/CDwUtkarsh/Diet-Recommendation-System.git

cd Diet-Recommendation-System
```

---

## 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 3️⃣ Run FastAPI Backend

```
cd FastAPI_Backend

uvicorn main:app --reload
```

FastAPI API docs will be available at:

```
http://127.0.0.1:8000/docs
```

---

## 4️⃣ Run Streamlit Frontend

```
streamlit run Streamlit_Frontend/Hello.py
```

Streamlit app will run at:

```
http://localhost:8501
```

---

# 📊 Example Output

The system generates:

• Personalized diet plans
• Recommended meals
• Nutrition breakdown
• Calories comparison chart
• Recipe ingredients and instructions

---

# 🎯 Future Improvements

* AI nutrition chatbot
* Weekly meal planner
* Macro nutrient optimization
* Food preference filtering
* Mobile responsive UI

---

# 👨‍💻 Author

**Utkarsh Tiwari**

GitHub
https://github.com/CDwUtkarsh

---

# ⭐ Support

If you like this project, please consider giving it a ⭐ on GitHub.
