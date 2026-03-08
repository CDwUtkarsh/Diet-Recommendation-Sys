import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity


class Generator:

    def __init__(self, nutrition_values):

        self.nutrition_values = nutrition_values

        # Load dataset
        self.dataset = pd.read_csv("Data/dataset_cleaned.csv")

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

        # Drop missing rows
        self.dataset = self.dataset.dropna(subset=self.nutrition_cols)

        # Initialize scaler
        self.scaler = StandardScaler()

        # Fit scaler
        self.dataset_scaled = self.scaler.fit_transform(self.dataset[self.nutrition_cols])

    def generate(self):

        # Convert input to dataframe
        input_df = pd.DataFrame(
            [self.nutrition_values],
            columns=self.nutrition_cols
        )

        # Scale input
        scaled_input = self.scaler.transform(input_df)

        # Calculate similarity
        similarity = cosine_similarity(scaled_input, self.dataset_scaled)

        # Top 5 recipes
        top_index = similarity[0].argsort()[-5:][::-1]

        result = self.dataset.iloc[top_index]

        return {
            "output": result.to_dict(orient="records")
        }