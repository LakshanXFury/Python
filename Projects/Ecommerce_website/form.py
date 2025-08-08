from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField
from wtforms.validators import DataRequired


class NewProduct(FlaskForm):
    product_name = StringField("Name of the Product you want to add .?", validators=[DataRequired()])
    product_price = StringField("The price of the product .?", validators=[DataRequired()])
    image_of_product = URLField("The Image url of the product ?", validators=[DataRequired()])
    submit_btn = SubmitField("Submit")


class DeleteProduct(FlaskForm):
    product_name = SelectField("Select the cafe that you want to Delete..!!!", choices=[])
    submit_btn = SubmitField("Delete")


