import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

class Generator:
    def __init__(self, nutrition_values):
        self.nutrition_values = nutrition_values
        self.dataset = pd.read_csv("Data/dataset.csv")

    def generate(self):
        # example logic
        return self.dataset.sample(5).to_dict(orient="records")
