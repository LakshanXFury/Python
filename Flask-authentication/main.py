from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
Bootstrap5(app)


# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE IN DB


class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register',  methods=["GET", "POST"])
def register():
    if request.method == "POST":
        register_new_user = User(
            email=request.form.get("email"),
            password=request.form.get("password"),
            name=request.form.get("name")
        )
        db.session.add(register_new_user)
        db.session.commit()
        # Passing over the user's name
        return render_template("secrets.html", name=request.form.get('name'))

    return render_template("register.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/secrets')
def secrets():

    return render_template("secrets.html")


@app.route('/logout')
def logout():
    pass


@app.route('/download')
# send_from_directory()
def download():
    return send_from_directory(directory="static", path="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
