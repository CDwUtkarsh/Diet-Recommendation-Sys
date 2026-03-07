import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

class Generator:

    def __init__(self, nutrition_values):

        self.nutrition_values = nutrition_values

        # Load dataset
        self.dataset = pd.read_csv(
            "Data/dataset.csv",
            encoding="latin1",
            engine="python",
            on_bad_lines="skip"
        )

        # Convert Nutrition column from string to list
        self.dataset["Nutrition"] = self.dataset["Nutrition"].apply(
            lambda x: eval(x) if isinstance(x, str) else x
        )

        # Create nutrition dataframe
        nutrition_df = pd.DataFrame(
            self.dataset["Nutrition"].tolist(),
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

        self.dataset = pd.concat([self.dataset, nutrition_df], axis=1)

        # Drop rows with missing values
        self.dataset = self.dataset.dropna(subset=nutrition_df.columns)

        # Scale features
        scaler = StandardScaler()
        self.scaled_data = scaler.fit_transform(self.dataset[nutrition_df.columns])

        self.target = scaler.transform([self.nutrition_values])


    def generate(self):

        similarity = cosine_similarity(self.target, self.scaled_data)

        top_indices = similarity[0].argsort()[-10:][::-1]

        recommendations = self.dataset.iloc[top_indices]

        return {"output": recommendations.to_dict(orient="records")}
