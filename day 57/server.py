from flask import Flask, render_template
from datetime import date
import requests

app = Flask(__name__)


@app.route("/")
def home():
    current_year = date.today().year
    return "Hello World"

@app.route("/guess/<name>")
def guess(name):
    name_guess = name.title()

    # genderize part
    genderize_url = f"https://api.genderize.io?name={name_guess}"
    gender_resposne = requests.get(genderize_url)
    gender_resposne.raise_for_status()
    gender_json = gender_resposne.json()
    gender = gender_json["gender"]

    # ageify part
    agify_url = f"https://api.agify.io?name={name_guess}"
    agify_response = requests.get(agify_url)
    agify_response.raise_for_status()
    agify_json = agify_response.json()
    age = agify_json["age"]


    return render_template("index.html", name=name_guess, gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)