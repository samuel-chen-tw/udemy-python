# This is a challenge in day 55

from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return "<b>" + function() + "</b>"
    return wrapper_function


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
@make_bold
def bye():
    return "Bye!"


if __name__ == "__main__":
    app.run(debug=True)
