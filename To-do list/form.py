from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, TimeField
from wtforms.validators import DataRequired, Length
from datetime import date, time


class NewTodo(FlaskForm):
    data_field = StringField(label="What do you want to be reminded about ??",
                             render_kw={"placeholder": "e.g., Call John at 5PM"},
                             validators=[DataRequired(), Length(max=30)])
    time_field = TimeField(label="Enter the time)",
                           validators=[DataRequired()])
    date_field = DateField(label="What is the deadline of you task ??",
                           render_kw={"placeholder": "Select a date", "min": date.today().isoformat()},
                           validators=[DataRequired()])
    submit = SubmitField("Submit")
