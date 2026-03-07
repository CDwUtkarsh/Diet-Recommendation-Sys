import pandas as pd
import streamlit as st
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity


@st.cache_data
def load_dataset():
    df = pd.read_csv("Data/dataset_small.csv")
    df.columns = df.columns.str.strip()
    return df


class Generator:

    def __init__(self, nutrition_values):

        self.nutrition_values = nutrition_values
        self.dataset = load_dataset()

        self.nutrition_cols = [
            "Calories",
            "FatContent",
            "SaturatedFatContent",
            "CholesterolContent",
            "SodiumContent",
            "CarbohydrateContent",
            "FiberContent",
            "SugarContent",
            "ProteinContent"
        ]

        scaler = StandardScaler()

        self.scaled_data = scaler.fit_transform(self.dataset[self.nutrition_cols])

        self.target = scaler.transform([nutrition_values])


    def generate(self):

        similarity = cosine_similarity(self.target, self.scaled_data)

        top_indices = similarity[0].argsort()[-10:][::-1]

        recommendations = self.dataset.iloc[top_indices]

        return {"output": recommendations.to_dict(orient="records")}
