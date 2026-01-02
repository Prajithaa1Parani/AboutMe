from flask import Flask, render_template
from profile import name, degree
from goals import goal

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        name=name,
        degree=degree,
        goal=goal
    )

if __name__ == "__main__":
    app.run(debug=True)
