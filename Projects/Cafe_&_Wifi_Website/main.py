from flask import Flask, flash, render_template, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from flask_bootstrap import Bootstrap5
from form import NewCafe, DeleteCafe, LoginForm, RegisterForm
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
Bootstrap5(app)

# Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


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
    __tablename__ = "cafe"
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


# Create a User table for all your registered users
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(100))


with app.app_context():
    db.create_all()


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # If I try to access Delete or Add Cafe, instead of crashing it redirects to Login
        if not current_user.is_authenticated:
            return redirect(url_for('login'))
        # If id is not 1 then return abort with 403 error
        if current_user.id != 1:
            return abort(403)
        # Otherwise continue with the route function
        return f(*args, **kwargs)

    return decorated_function


@app.route("/")
def get_all_cafe():
    # READ ALL RECORDS
    # Construct a query to select from the database. Returns the rows in the database
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    # Use .scalars() to get the elements rather than entire rows from the database
    all_cafes = result.scalars().all()
    return render_template("index.html", cafes=all_cafes)  # 1 is TRUE and 0 is FALSE


@app.route("/add-cafe", methods=["GET", "POST"])
@admin_only
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


@app.route("/delete", methods=["GET", "POST"])
@admin_only
def delete_cafe():
    # cafe_form = DeleteCafe()
    # if cafe_form.validate_on_submit():
    #     cafe_to_delete = db.session.execute(db.select(Cafe).where(Cafe.name == cafe_form.name.data)).scalar_one_or_none()
    #
    #     if cafe_to_delete:
    #         db.session.delete(cafe_to_delete)
    #         db.session.commit()
    #         return redirect(url_for("get_all_cafe"))
    #     else:
    #         return render_template("delete_cafe.html", form=cafe_form, not_found=True)
    #
    # return render_template("delete_cafe.html", form=cafe_form)

    # Using Flask Flash
    cafe_form = DeleteCafe()
    not_found = False

    if cafe_form.validate_on_submit():
        cafe_name = cafe_form.name.data
        cafe_to_delete = db.session.execute(db.select(Cafe).where(Cafe.name == cafe_name)).scalar()

        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            flash(f"Cafe '{cafe_name}' was deleted successfully!", "success")
            return redirect(url_for("get_all_cafe"))  # Redirect to list page
        else:
            flash(f"No cafe found with the name '{cafe_name}'.", "warning")
            not_found = True

    return render_template("delete_cafe.html", form=cafe_form, not_found=not_found)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():

        # Check if user email is already present in the database.
        result = db.session.execute(db.select(User).where(User.email == form.email.data))
        user = result.scalar()
        if user:
            # User already exists
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        hash_and_salted_password = generate_password_hash(
            form.password.data,
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            email=form.email.data,
            name=form.name.data,
            password=hash_and_salted_password,
        )
        db.session.add(new_user)
        db.session.commit()
        # This line will authenticate the user with Flask-Login
        login_user(new_user)
        return redirect(url_for("get_all_cafe"))
    return render_template("register.html", form=form, current_user=current_user)


"""
Admin account email: lakshan@gmail.com

Admin account password: test@123

"""


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        password = form.password.data
        result = db.session.execute(db.select(User).where(User.email == form.email.data))
        # Note, email in db is unique so will only have one result.
        user = result.scalar()
        # Email doesn't exist
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        # Password incorrect
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('get_all_cafe'))
    return render_template("login.html", form=form, current_user=current_user)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_cafe'))


if __name__ == '__main__':
    app.run(debug=True)
