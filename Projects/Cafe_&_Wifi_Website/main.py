from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from flask_bootstrap import Bootstrap5
from form import NewCafe

app = Flask(__name__)
Bootstrap5(app)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db?timeout=10'  #This sets a 10-second timeout, allowing SQLite to wait before raising a locked error.
db = SQLAlchemy(model_class=Base)
db.init_app(app)

#Secret Key for CSRF
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Integer, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Integer, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Integer, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Integer, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

        # # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        # return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def get_all_cafe():
    ##READ ALL RECORDS
    # Construct a query to select from the database. Returns the rows in the database
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    # Use .scalars() to get the elements rather than entire rows from the database
    all_cafes = result.scalars().all()
    return render_template("index.html", cafes=all_cafes)  # 1 is TRUE and 0 is FALSE


@app.route("/add-cafe", methods=["GET", "POST"])
def add_cafe():
    cafe_form = NewCafe()

    if cafe_form.validate_on_submit():
        new_cafe = Cafe(
            name=cafe_form.name.data,
            map_url=cafe_form.map_url.data,
            img_url=cafe_form.image_url.data,
            location=cafe_form.location.data,
            has_sockets=int(cafe_form.sockets.data),
            has_wifi=int(cafe_form.wifi.data),
            can_take_calls=int(cafe_form.take_calls.data),
            has_toilet=int(cafe_form.toilets.data),
            seats=cafe_form.seats.data,
            coffee_price=cafe_form.coffee_price.data
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for("get_all_cafe"))
    return render_template("add_cafe.html", form=cafe_form)


if __name__ == '__main__':
    app.run(debug=True)
