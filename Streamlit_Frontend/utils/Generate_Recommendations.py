import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st


# Cache dataset loading
@st.cache_data
def load_dataset():
    url = "https://huggingface.co/datasets/utkarsh121254/diet-recommendation-dataset/resolve/main/dataset_cleaned.csv"
    df = pd.read_csv(url)

    nutrition_cols = [
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

    df = df.dropna(subset=nutrition_cols)

    return df


# Cache scaler + scaled dataset
@st.cache_resource
def prepare_model(dataset, nutrition_cols):

    scaler = StandardScaler()

    dataset_scaled = scaler.fit_transform(dataset[nutrition_cols])

    return scaler, dataset_scaled


class Generator:

    def __init__(self, nutrition_values):

        self.nutrition_values = nutrition_values

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
            "ProteinContent"
        ]

        # Load dataset (cached)
        self.dataset = load_dataset()

        # Prepare scaler + scaled data (cached)
        self.scaler, self.dataset_scaled = prepare_model(
            self.dataset, self.nutrition_cols
        )

    def generate(self):

        # Convert input to dataframe
        input_df = pd.DataFrame(
            [self.nutrition_values],
            columns=self.nutrition_cols
        )

        # Scale input
        scaled_input = self.scaler.transform(input_df)

        # Cosine similarity
        similarity = cosine_similarity(
            scaled_input, self.dataset_scaled
        )

        # Top 5 similar recipes
        top_index = similarity[0].argsort()[-5:][::-1]

        result = self.dataset.iloc[top_index]

        return {
            "output": result.to_dict(orient="records")
        }