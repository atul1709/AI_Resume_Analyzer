def generate_feedback(skills, missing_skills, career):
    feedback = []

    if len(skills) < 6:
        feedback.append("Add more technical skills relevant to your target role.")

    if missing_skills:
        feedback.append(
            f"Consider adding these skills for {career}: " + ", ".join(missing_skills)
        )

    feedback.append("Add 2–3 real-world projects with measurable impact.")
    feedback.append("Use action verbs like Designed, Implemented, Optimized.")

    return feedback
