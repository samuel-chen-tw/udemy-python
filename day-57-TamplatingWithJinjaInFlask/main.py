from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    posts = requests.get("https://api.npoint.io/ae8381106e429586df99").json()
    return render_template("index.html", posts=posts)


@app.route("/post/<int:num>")
def get_post(num):
    posts = requests.get("https://api.npoint.io/ae8381106e429586df99").json()
    print(num)
    print(posts)
    post = next((post for post in posts if post.get('id') == num), None)
    print(post)
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
