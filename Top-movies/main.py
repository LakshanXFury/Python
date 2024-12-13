from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

api_key = "61e528dacff24903d942a0faf48300a2"
url = "https://api.themoviedb.org/3/search/movie"


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class Base(DeclarativeBase):
    pass


# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies_collection.db"

db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE DB
class Movie(db.Model):
    """nullable=True: The column can have NULL values. It is optional.
        nullable=False: The column cannot have NULL values. It is mandatory."""
    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # mapped for type check
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[str] = mapped_column(String(250), nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


with app.app_context():
    db.create_all()


class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")


class AddMovies(FlaskForm):
    title_movie = StringField("Add New Movie")
    submit = SubmitField("Add Movie")


# CREATE TABLE


@app.route("/")
def home():
    ##READ ALL RECORDS
    # Construct a query to select from the database. Returns the rows in the database
    result = db.session.execute(db.select(Movie).order_by(Movie.title))
    # Use .scalars() to get the elements rather than entire rows from the database
    all_movies = result.scalars().all()
    print(all_movies)
    return render_template("index.html", movies=all_movies)


#Edit Movie rating & review
@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")  # gets the id from the url which is being sent
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get('id')  # gets the id from the url which is being sent
    print(movie_id)
    movie_to_delete = db.get_or_404(Movie, movie_id)

    # Alternative way to select the book to delete.
    # book_to_delete = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
    db.session.delete(movie_to_delete)
    db.session.commit()

    return redirect(url_for("home"))


@app.route("/add_movie", methods=["GET", "POST"])
def add_movie():
    form = AddMovies()

    if form.validate_on_submit():
        movie_title = form.title_movie.data
        response = requests.get(url=url, params={"query": movie_title, "api_key": api_key, "language": "en-US"})
        api_response = response.json()['results']
        return render_template("select.html", data=api_response)
    
    return render_template("add.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
