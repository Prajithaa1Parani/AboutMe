from flask import Flask, render_template
from resume_data import name, degree, skills, goal

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        name=name,
        degree=degree,
        goal=goal
    )
@app.route("/resume")
def resume():
    return render_template(
        "resume.html",
        name=name,
        degree=degree,
        skills=skills,
        goal=goal
    )


if __name__ == "__main__":
    app.run(debug=True)
