from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():

    aptitude = 65
    programming = 45
    companies = 30

    # Calculate overall progress automatically
    overall = round((aptitude + programming + companies) / 3)

    return render_template(
        "index.html",
        aptitude=aptitude,
        programming=programming,
        companies=companies,
        overall=overall
    )


app.run(debug=True)