from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length, NumberRange
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///fav_movies.db"

Bootstrap(app)
db = SQLAlchemy(app)

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Float, nullable=False)
    review = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)

class RateMovieForm(FlaskForm):
    rating = FloatField('Rating', validators=[DataRequired(), NumberRange(min=1, max=10)])
    review = StringField('Review', validators=[DataRequired(), Length(max=50)])
    submit = SubmitField()

with app.app_context():
    db.create_all()


def movie_to_db():
    new_movie = Movies(
        title="Avatar The Way of Water",
        year=2022,
        description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
        rating=7.3,
        ranking=9,
        review="I liked the water.",
        img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
    )

    with app.app_context():
        db.session.add(new_movie)
        db.session.commit()


def read_all_db():
    with app.app_context():
        result = db.session.execute(db.select(Movies).order_by(Movies.id))
        all_movies = result.scalars()
        movies_list = []
        for movie in all_movies:
            movies_list.append({
                "id": movie.id,
                "title": movie.title,
                "year": movie.year,
                "description": movie.description,
                "rating": movie.rating,
                "ranking": movie.ranking,
                "review": movie.review,
                "img_url": movie.img_url,
                })
        return movies_list


def find_movie_in_db(id):
    with app.app_context():
        movie = db.session.execute(db.select(Movies).where(Movies.id == id)).scalar()
        return movie
    

def update_movie(id, new_rating, new_review):
    with app.app_context():
        movie = db.session.execute(db.select(Movies).where(Movies.id == id)).scalar()
        movie.rating = new_rating
        movie.review= new_review
        db.session.commit()
    

def delmovie_in_db(id):
    with app.app_context():
        movie = db.session.execute(db.select(Movies).where(Movies.id == id)).scalar()
        db.session.delete(movie)
        db.session.commit()


# movie_to_db()

@app.route("/")
def home():
    movies = read_all_db()
    return render_template("index.html", movies=movies)

@app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    form = RateMovieForm()
    movie = find_movie_in_db(id)

    if form.validate_on_submit():
        new_rating = form.rating.data
        new_review = form.review.data
        update_movie(id, new_rating, new_review)
        return redirect(url_for("home"))

    return render_template("edit.html", movie=movie, form=form)


@app.route("/del/<id>", methods=["GET", "POST"])
def delete_movie(id):
    delmovie_in_db(id)
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run()
