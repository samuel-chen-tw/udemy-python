import random

from flask import Flask

app = Flask(__name__)

rand_num = random.randint(0, 9)
print(rand_num)


@app.route("/")
def homepage():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"/>'


@app.route("/<int:num>")
def guess_number(num):
    if rand_num == num:
        return '<h1>You found me!</h1>' \
               '</h1><img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"/>'
    elif rand_num > num:
        return '<h1 style="color: red">Too low, try again!' \
               '</h1><img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"/>'
    else:
        return '<h1 style="color: purple">Too high, try again!</h1>' \
               '</h1><img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"/>'


if __name__ == "__main__":
    app.run(debug=True)
