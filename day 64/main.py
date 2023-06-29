from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length, NumberRange
import requests
from dotenv import dotenv_values

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///fav_movies.db"

Bootstrap(app)
db = SQLAlchemy(app)

config = dotenv_values(".env")
MOVIE_DB_TOKEN = config['MOVIE']

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


class RateMovieForm(FlaskForm):
    rating = FloatField('Rating', validators=[DataRequired(), NumberRange(min=1, max=10)])
    review = StringField('Review', validators=[DataRequired(), Length(max=50)])
    submit = SubmitField()


class AddMoveTitle(FlaskForm):
    movie_title = StringField('Movie Title', validators=[DataRequired(), Length(max=50)])
    submit = SubmitField('Add Movie')

with app.app_context():
    db.create_all()


def read_all_db():
    with app.app_context():
        result = db.session.execute(db.select(Movies).order_by(Movies.rating))
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


@app.route("/")
def home():
    movies = read_all_db()
    return render_template("index.html", movies=movies)

@app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    form = RateMovieForm()
    movie = find_movie_in_db(id)

    if request.method == "POST":
        print(id)

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


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMoveTitle()
    if request.method == "POST":
        movie_to_search = form.movie_title.data

        url = f"https://api.themoviedb.org/3/search/movie?query={movie_to_search}&include_adult=false&language=en-US&page=1"

        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {MOVIE_DB_TOKEN}"
        }

        response = requests.get(url, headers=headers).json()["results"]
        return render_template("select.html", movies=response)

    return render_template("add.html", form=form)

@app.route("/find")
def search_meta():
    api_id = request.args.get("id")
    url = f"https://api.themoviedb.org/3/movie/{api_id}?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {MOVIE_DB_TOKEN}"
    }

    response = requests.get(url, headers=headers).json()

    movie_meta = Movies(
        title=response["title"],
        year=response["release_date"].split("-")[0],
        description=response["overview"],
        img_url=f"https://image.tmdb.org/t/p/w500{response['poster_path']}"
    )

    with app.app_context():
        db.session.add(movie_meta)
        db.session.commit()
        movie = db.session.execute(db.select(Movies).where(Movies.title == response["title"])).scalar()

    return redirect(url_for("edit", id=movie.id))


if __name__ == '__main__':
    app.run()
