from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_ats_score(resume_text, jd_text=None, benchmark_text=None):
    vectorizer = TfidfVectorizer(stop_words="english")

    if jd_text and jd_text.strip():
        texts = [resume_text, jd_text]
    else:
        texts = [resume_text, benchmark_text]

    vectors = vectorizer.fit_transform(texts)
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

    score = round(similarity * 100, 2)

    tips = []
    if score < 40:
        tips.append("Add more role-specific keywords and projects.")
    if score < 60:
        tips.append("Improve project descriptions with measurable results.")
    if score < 80:
        tips.append("Optimize resume formatting and section clarity.")

    return score, tips
