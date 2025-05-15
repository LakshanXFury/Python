from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired


class NewTodo(FlaskForm):
    data_field = StringField(label="What do you want to be reminded about ??", validators=[DataRequired()])
    date_field = DateField(label="What is the deadline of you task ??", validators=[DataRequired])
    submit = SubmitField("Submit")

