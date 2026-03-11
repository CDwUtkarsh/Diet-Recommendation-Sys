

---

# 🥗 NutriGenie – AI Diet Recommendation System

**NutriGenie** is an AI-powered diet recommendation system that generates personalized meal plans based on a user's body metrics, activity level, and weight goals.

The application leverages **Machine Learning, FastAPI, and Streamlit** to recommend healthy meals, analyze nutritional values, and provide recipe guidance through an interactive interface.

---

# 🌐 Live Demo

🚀 **Try the App**

[https://diet-recommendation-sys-zjmv4fwfsuzjx2aykux6wf.streamlit.app/](https://diet-recommendation-sys-zjmv4fwfsuzjx2aykux6wf.streamlit.app/)

---

# 📊 Dataset

The system uses a cleaned food dataset containing recipe information and nutritional values.

📁 Dataset Source:

[https://huggingface.co/datasets/utkarsh121254/diet-recommendation-dataset/resolve/main/dataset_cleaned.csv](https://huggingface.co/datasets/utkarsh121254/diet-recommendation-dataset/resolve/main/dataset_cleaned.csv)

---

# 🚀 Features

* ✅ Personalized diet recommendations based on user metrics
* ✅ BMI calculation and body health insights
* ✅ Daily calorie requirement estimation
* ✅ AI-powered meal recommendations
* ✅ Detailed recipe ingredients and cooking instructions
* ✅ Nutritional value breakdown for each meal
* ✅ Meal image preview
* ✅ Interactive nutrition visualization charts

---

# 🧠 Tech Stack

| Technology            | Purpose                                |
| --------------------- | -------------------------------------- |
| **Python**            | Core programming language              |
| **Streamlit**         | Frontend user interface                |
| **FastAPI**           | Backend API                            |
| **Scikit-Learn**      | Machine learning recommendation engine |
| **Pandas**            | Data preprocessing and analysis        |
| **Streamlit ECharts** | Interactive visualization              |

---

# 🏗 System Architecture

```
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
Nutrition Visualization & Meal Suggestions
```

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

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/CDwUtkarsh/Diet-Recommendation-System.git

cd Diet-Recommendation-System
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Run FastAPI Backend

```bash
cd FastAPI_Backend

uvicorn main:app --reload
```

FastAPI API documentation:

```
http://127.0.0.1:8000/docs
```

---

## 4️⃣ Run Streamlit Frontend

```bash
streamlit run Streamlit_Frontend/Hello.py
```

App will run at:

```
http://localhost:8501
```

---

# 📊 Example Output

The system generates:

* Personalized diet plans
* Recommended meals based on nutritional targets
* Nutrition breakdown for each recipe
* Calorie comparison charts
* Detailed ingredients and cooking instructions

---

# 🎯 Future Improvements

* 🤖 AI nutrition chatbot
* 📅 Weekly meal planner
* ⚖ Macro-nutrient optimization
* 🥗 Food preference & allergy filtering
* 📱 Mobile responsive UI

---

# 👨‍💻 Author

**Utkarsh Tiwari**

GitHub
[https://github.com/CDwUtkarsh](https://github.com/CDwUtkarsh)

---

# ⭐ Support

If you found this project useful, please consider giving it a **⭐ on GitHub**.

---


