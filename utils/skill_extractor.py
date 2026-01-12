SKILLS = [
    "python", "sql", "excel", "statistics",
    "data analysis", "machine learning", "deep learning",
    "html", "css", "javascript", "react", "node",
    "flask", "django", "java", "spring",
    "docker", "kubernetes", "aws", "azure",
    "selenium", "automation testing", "qa",
    "power bi", "tableau",
    "cybersecurity", "network security",
    "android", "kotlin"
]

def extract_skills(text):
    return list(set(skill for skill in SKILLS if skill in text))
