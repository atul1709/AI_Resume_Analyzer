# AI Resume Analyzer

AI Resume Analyzer is a Machine Learning–based web application that evaluates resumes for ATS (Applicant Tracking System) compatibility, predicts suitable career paths with confidence scores, and provides actionable feedback to improve resume quality.

## Key Features
- ATS score calculation using ML-based text similarity
- Top-3 career predictions with confidence percentages
- Resume analysis with or without job description
- Automated resume improvement suggestions
- Skill extraction and industry benchmark comparison
- Responsive and user-friendly web interface

## Machine Learning Approach
- TF-IDF vectorization for resume and job description representation
- Cosine similarity for ATS scoring
- Logistic Regression for multi-career classification
- Probability-based predictions to avoid biased career results

## Tech Stack
- Backend: Python, Flask  
- Machine Learning: Scikit-learn, TF-IDF, Logistic Regression  
- Frontend: HTML, CSS, Bootstrap  
- Resume Parsing: PyMuPDF  

## How to Run
```bash
pip install -r requirements.txt
python train_models.py
python app.py
