import pandas as pd
import streamlit as st
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity


@st.cache_data
def load_dataset():
    df = pd.read_csv(
        "Data/dataset.csv",
        encoding="latin1",
        sep=",",
        engine="python",
        on_bad_lines="skip",
        quoting=3
    )
    return df


class Generator:

    def __init__(self, nutrition_values):

        self.nutrition_values = nutrition_values

        # Load dataset
        self.dataset = load_dataset()

        # Nutrition columns
        self.nutrition_cols = [
            "Calories",
            "FatContent",
            "SaturatedFatContent",
            "CholesterolContent",
            "SodiumContent",
            "CarbohydrateContent",
            "FiberContent",
            "SugarContent",
            "ProteinContent",
        ]

        # Drop missing rows
        self.dataset = self.dataset.dropna(subset=self.nutrition_cols)

        # Scale features
        scaler = StandardScaler()
        self.scaled_data = scaler.fit_transform(self.dataset[self.nutrition_cols])

        self.target = scaler.transform([nutrition_values])


    def generate(self):

        similarity = cosine_similarity(self.target, self.scaled_data)

        top_indices = similarity[0].argsort()[-10:][::-1]

        recommendations = self.dataset.iloc[top_indices]

        return {"output": recommendations.to_dict(orient="records")}
