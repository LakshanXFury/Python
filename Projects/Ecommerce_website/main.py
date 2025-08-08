from flask import Flask, request, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from form import NewProduct, DeleteProduct

app = Flask(__name__)
Bootstrap5(app)


# CREATE DB
class Base(DeclarativeBase):
    pass


#Secret Key for CSRF
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

# Connect to Database
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db?timeout=10'  #This sets a 10-second timeout, allowing SQLite to wait before raising a locked error.
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Product(db.Model):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    product_image: Mapped[str] = mapped_column(nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add-product", methods=["GET", "POST"])
def add_product():
    new_product = NewProduct()
    if new_product.validate_on_submit():
        product = Product(
            name=new_product.product_name.data,
            price=new_product.product_price.data,
            product_image=new_product.image_of_product.data
        )
        db.session.add(product)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_product.html", form=new_product)


@app.route("/delete", methods=["GET", "POST"])
def delete_product():
    form = DeleteProduct()
    form.product_name.choices = [(p.id, f"{p.name} - ₹{p.price}") for p in Product.query.all()]
    # You're not seeing p.id in the frontend dropdown because it's not meant to be displayed —
    # it's being used as the value behind the scenes.
    # (value_submitted, label_displayed)
    
    if form.validate_on_submit():
        product_to_delete = Product.query.filter_by(name=form.product_name.data).first()
        if product_to_delete:
            db.session.delete(product_to_delete)
            db.session.commit()
            return redirect(url_for("home"))

    return render_template("delete_product.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
