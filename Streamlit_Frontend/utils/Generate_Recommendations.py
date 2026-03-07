import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

class Generator:

    def __init__(self, nutrition_values):
        self.nutrition_values = nutrition_values
        
        # Load dataset
        self.dataset = pd.read_csv(
            "Data/dataset.csv",
            encoding="latin1",
            engine="python",
            on_bad_lines="skip",
            low_memory=False
        )

        # Nutrition columns
        self.nutrition_cols = [
            'Calories','FatContent','SaturatedFatContent',
            'CholesterolContent','SodiumContent',
            'CarbohydrateContent','FiberContent',
            'SugarContent','ProteinContent'
        ]

        # Clean dataset
        self.dataset = self.dataset.dropna(subset=self.nutrition_cols)

        # Scale nutrition data
        scaler = StandardScaler()
        self.scaled_data = scaler.fit_transform(self.dataset[self.nutrition_cols])

        # Target nutrition vector
        self.target = scaler.transform([self.nutrition_values])

    def generate(self):

        # Calculate similarity
        similarity = cosine_similarity(self.target, self.scaled_data)

        # Get top recipes
        top_indices = similarity[0].argsort()[-10:][::-1]

        recommendations = self.dataset.iloc[top_indices]

        result = recommendations.to_dict(orient="records")

        return {"output": result}
