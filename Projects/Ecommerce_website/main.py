import os

from flask import Flask, request, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from form import NewProduct, DeleteProduct
from dotenv import load_dotenv
import stripe

app = Flask(__name__)
Bootstrap5(app)


# CREATE DB
class Base(DeclarativeBase):
    pass


#Secret Key for CSRF
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

# Connect to Database
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db?timeout=10'  #This sets a 10-second timeout, allowing SQLite
# to wait before raising a locked error.
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

# 🔑 Stripe keys (use your own test keys from dashboard)
stripe.api_key = os.getenv("Secret_key")  # Secret Key
PUBLISHABLE_KEY = os.getenv("Publishable_key")  # Publishable Key


@app.route("/")
def home():
    # Read all the records
    result = db.session.execute(db.select(Product).order_by(Product.name))
    # Use .scalars() to get the elements rather than entire rows from the database
    all_products = result.scalars().all()
    return render_template("index.html", products=all_products)


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


# 🟢 Stripe Checkout Integration
@app.route("/create-checkout-session/<int:product_id>", methods=["POST"])
def create_checkout_session(product_id):
    product = Product.query.get(product_id)
    if not product:
        return "Product not found", 404

    try:
        # Stripe Checkout session
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[{
                "price_data": {
                    "currency": "usd",
                    "product_data": {"name": product.name},
                    "unit_amount": int(product.price * 100),  # Stripe expects cents
                },
                "quantity": 1,
            }],
            mode="payment",
            success_url=url_for("success", _external=True),
            cancel_url=url_for("cancel", _external=True),
        )
        return redirect(session.url, code=303)

    except Exception as e:
        return str(e)


@app.route("/success")
def success():
    return "✅ Payment successful! Thank you for your purchase."


@app.route("/cancel")
def cancel():
    return "❌ Payment canceled. Please try again."


if __name__ == "__main__":
    app.run(debug=True)
