from flask import Flask, render_template
import requests

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/36450fe90991ae6bc4c8").json()


@app.route("/")
def home():
    return render_template("index.html", all_posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:num>')
def post(num):
    post_data = next((post_data for post_data in posts if post_data['id'] == num))
    print(post_data)
    return render_template('post.html', post=post_data)


if __name__ == "__main__":
    app.run(debug=True)
