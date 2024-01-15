from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

NAME = "Samuel Chen"


@app.route("/")
def home():
    random_number = random.randint(1, 9)
    year = datetime.now().year
    return render_template("index.html", num=random_number, name=NAME, year=year)


@app.route("/guess/<name>")
def guess_name(name):
    age = requests.get(f"https://api.agify.io?name={name}").json().get("age")
    gender = requests.get(f"https://api.genderize.io?name={name}").json().get("gender")
    return render_template("guess.html", name=name, age=age, gender=gender)


@app.route("/blog/<num>")
def get_blog(num):
    posts = requests.get("https://api.npoint.io/ae8381106e429586df99").json()
    print(num)
    return render_template("blog.html", posts=posts)


if __name__ == "__main__":
    app.run(debug=True)
