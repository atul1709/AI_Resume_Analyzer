import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import os

data = pd.read_csv("data/training_data.csv")

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data["skills"])
y = data["career"]

model = LogisticRegression(max_iter=1000)
model.fit(X, y)

os.makedirs("models", exist_ok=True)
pickle.dump((vectorizer, model), open("models/career_classifier.pkl", "wb"))

print("✅ Multi-career ML model trained successfully")
