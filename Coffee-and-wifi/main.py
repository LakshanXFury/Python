from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, URLField
from wtforms.validators import DataRequired, URL
import csv

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    cafe_location = URLField('Cafe location', validators=[DataRequired(), URL()])
    opening_time = StringField('Opening time Ex:->8am', validators=[DataRequired()])
    closing_time = StringField('Closing time Ex:->5pm', validators=[DataRequired()])
    coffe_rating = SelectField('Coffee Rating', choices=[('☕️', '☕️'), ('☕️☕️', '☕️☕️'),
                                                         ('☕️☕️☕️', '☕️☕️☕️'),('☕️☕️☕️☕️', '☕️☕️☕️☕️'),
                                                         ('☕️☕️☕️☕️☕️', '☕️☕️☕️☕️☕️')])
    wifi_rating = SelectField('Wifi Strength Rating', choices=[('✘', '✘'), ('💪', '💪'),
                                                         ('💪💪', '💪💪' ),('💪💪💪', '💪💪💪'),
                                                         ('💪💪💪💪', '💪💪💪💪')])
    power_socket = SelectField('Wifi Strength Rating', choices=[('✘', '✘'), ('🔌', '🔌'),
                                                         ('🔌🔌', '🔌🔌'),('🔌🔌🔌', '🔌🔌🔌'),
                                                         ('🔌🔌🔌🔌', '🔌🔌🔌🔌')])

    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        # print("True")
        # print(form.cafe.data)
        new_row = [
            form.cafe.data,
            form.cafe_location.data,
            form.opening_time.data,
            form.closing_time.data,
            form.coffe_rating.data,
            form.wifi_rating.data,
            form.power_socket.data
        ]
        with open("cafe-data.csv", mode="a", newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(new_row)

        return redirect(url_for('add_cafe'))

    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.DictReader(csv_file)
        #uses the first row of the CSV file as keys for the dictionaries.
        # This allows you to use field names like cafe['Cafe Name'] in the template.
        list_of_rows = []
        for row in csv_data:
            print(row)
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
