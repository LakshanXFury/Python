from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

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


# CREATE TABLE


@app.route("/")
def home():
    ##READ ALL RECORDS
    # Construct a query to select from the database. Returns the rows in the database
    result = db.session.execute(db.select(Movie).order_by(Movie.title))
    # Use .scalars() to get the elements rather than entire rows from the database
    all_movies = result.scalars().all()
    print(all_movies)
    return render_template("index.html", movies = all_movies )


# def add_data():
#     with app.app_context():
#         second_movie = Movie(
#             title="Avatar The Way of Water",
#             year=2022,
#             description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#             rating=7.3,
#             ranking=9,
#             review="I liked the water.",
#             img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
#         )
#         db.session.add(second_movie)
#         db.session.commit()
#
# add_data()


if __name__ == '__main__':
    app.run(debug=True)
