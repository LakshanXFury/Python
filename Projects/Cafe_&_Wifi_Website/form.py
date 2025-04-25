from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, BooleanField, PasswordField, EmailField
from wtforms.validators import DataRequired


class NewCafe(FlaskForm):
    name = StringField("Name of the Cafe", validators=[DataRequired()])
    map_url = URLField("Map Url", validators=[DataRequired()])
    image_url = URLField("Image URL")
    location = StringField("Location of the Cafe", validators=[DataRequired()])
    sockets = BooleanField("Has Sockets ???", false_values=(False, "false", "no", "0"))
    toilets = BooleanField("Has Toilets in the premises ???", false_values=(False, "false", "no", "0"))
    wifi = BooleanField("Has Wifi in the premises", false_values=(False, "false", "no", "0"))
    take_calls = BooleanField("Can take call in the premises", false_values=(False, "false", "no", "0"))
    seats = StringField("No of approximate seats available in the premises", validators=[DataRequired()])
    coffee_price = StringField("Avg Coffee price in that cafe", validators=[DataRequired()])
    submit = SubmitField("Submit")


class DeleteCafe(FlaskForm):
    name = StringField("Name of the Cafe you want to Delete", validators=[DataRequired()])
    submit = SubmitField("Delete Cafe")


# Create a form to register new users
class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")


# Create a form to login existing users
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In!")
