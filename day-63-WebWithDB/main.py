from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)


# below use the sqlite3
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()


class Base(DeclarativeBase):
    pass


# create the extension
db = SQLAlchemy(model_class=Base)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# initialize the app with the extension
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


with app.app_context():
    db.create_all()


# CREATE RECORD
# with app.app_context():
#     new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
#     db.session.add(new_book)
#     db.session.commit()


@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    print(all_books)
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        with app.app_context():
            new_book = Book(title=request.form["title"], author=request.form["author"], rating=request.form["rating"])
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        update_book = db.get_or_404(Book, book_id)
        update_book.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for("home"))
    else:
        book_id = request.args.get('id')
        book = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        return render_template("edit.html", book=book)


@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    delete_book = db.get_or_404(Book, book_id)
    db.session.delete(delete_book)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
