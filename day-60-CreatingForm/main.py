from flask import Flask, render_template, request
import requests
import smtplib

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/36450fe90991ae6bc4c8").json()

MY_EMAIL = "samuel811215@gmail.com"
MY_PASSWORD = "zrcusgixpsqhgwul"

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    elif request.method == "POST":
        name = request.form['name']
        print(name)
        email = request.form['email']
        print(email)
        phone = request.form['phone']
        print(phone)
        message = request.form['message']
        print(message)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="samuel.chen@taiwanlife.com",
                msg=f"Subject:Message\n\nName: {name}\nEmail: {email}\nPhone:{phone}\nMessage: {message}"
            )
        return render_template("contact.html", success="Successfully sent message")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
