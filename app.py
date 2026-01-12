from flask import Flask, render_template, request
from utils.resume_parser import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.ml_ats_scorer import calculate_ats_score
from utils.career_ml import predict_top_careers
from utils.feedback_generator import generate_feedback

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        resume = request.files["resume"]
        job_desc = request.form.get("job_desc", "").lower()

        resume_text = extract_text_from_pdf(resume)
        resume_skills = extract_skills(resume_text)

        with open("data/industry_benchmark.txt") as f:
            benchmark = f.read().lower()

        ats_score, ats_tips = calculate_ats_score(
            resume_text, job_desc, benchmark
        )

        top_careers = predict_top_careers(resume_skills)

        missing_skills = []
        if job_desc.strip():
            missing_skills = list(
                set(extract_skills(job_desc)) - set(resume_skills)
            )

        feedback = generate_feedback(
            resume_skills, missing_skills, top_careers[0]["career"]
        )

        return render_template(
            "result.html",
            ats=ats_score,
            ats_tips=ats_tips,
            skills=resume_skills,
            top_careers=top_careers,
            feedback=feedback
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
