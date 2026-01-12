import pickle
import numpy as np

vectorizer, model = pickle.load(open("models/career_classifier.pkl", "rb"))

def predict_top_careers(skills, top_n=3):
    skills_text = " ".join(skills)
    vector = vectorizer.transform([skills_text])

    probabilities = model.predict_proba(vector)[0]
    classes = model.classes_

    ranked = sorted(
        zip(classes, probabilities),
        key=lambda x: x[1],
        reverse=True
    )

    return [
        {"career": c, "confidence": round(p * 100, 2)}
        for c, p in ranked[:top_n]
    ]
