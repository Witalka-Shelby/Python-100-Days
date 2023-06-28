from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy


def book_to_db(name, author, rating):
    ### add book to db
    book = Books(title = name, author = author, rating = rating)

    with app.app_context():
        db.session.add(book)
        db.session.commit()


def read_all_db():
    with app.app_context():
        result = db.session.execute(db.select(Books).order_by(Books.title))
        all_books = result.scalars()
        book_list = []
        for book in all_books:
            book_list.append({
                "id": book.id,
                "title": book.title,
                "author": book.author,
                "rating": book.rating
                })
        return book_list
    

def find_book_in_db(id):
    with app.app_context():
        result = db.session.execute(db.select(Books).where(Books.id == id))
        book = result.scalar()
        return book


def update_rating(id, new_rating):
    with app.app_context():
        book_to_update = db.session.execute(db.select(Books).where(Books.id == id)).scalar()
        book_to_update.rating = new_rating
        db.session.commit()


def delete_book(id):
    with app.app_context():
        book_to_del = db.session.execute(db.select(Books).where(Books.id == id)).scalar()
        db.session.delete(book_to_del)
        db.session.commit()


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    all_books = read_all_db()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form["book_name"]
        author = request.form["book_author"]
        rating = request.form["rating"]
        book_to_db(name, author, rating)
        return redirect(url_for("home"))
    
    return render_template("add.html")

@app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    if request.method == "POST":
        new_rating = request.form["new_rating"]
        update_rating(id, new_rating)
        return redirect(url_for("home"))

    book = find_book_in_db(id)
    return render_template("edit.html", book=book)

@app.route("/del/<id>")
def delete(id):
    delete_book(id)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()
