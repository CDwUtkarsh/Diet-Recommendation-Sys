import pandas as pd
import streamlit as st
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
import ast


@st.cache_data
def load_dataset():
    df = pd.read_csv(
        "Data/dataset.csv",
        encoding="latin1",
        engine="python",
        on_bad_lines="skip"
    )

    # Convert Nutrition string list to python list
    df["Nutrition"] = df["Nutrition"].apply(lambda x: ast.literal_eval(x))

    nutrition_df = pd.DataFrame(
        df["Nutrition"].tolist(),
        columns=[
            "Calories",
            "FatContent",
            "SaturatedFatContent",
            "CholesterolContent",
            "SodiumContent",
            "CarbohydrateContent",
            "FiberContent",
            "SugarContent",
            "ProteinContent",
        ],
    )

    df = pd.concat([df, nutrition_df], axis=1)

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
            "ProteinContent",
        ]

        # remove missing rows
        self.dataset = self.dataset.dropna(subset=self.nutrition_cols)

        scaler = StandardScaler()

        self.scaled_data = scaler.fit_transform(self.dataset[self.nutrition_cols])

        self.target = scaler.transform([nutrition_values])


    def generate(self):

        similarity = cosine_similarity(self.target, self.scaled_data)

        top_indices = similarity[0].argsort()[-10:][::-1]

        recommendations = self.dataset.iloc[top_indices]

        return {"output": recommendations.to_dict(orient="records")}
