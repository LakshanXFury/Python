from flask import Flask, flash, render_template, redirect, url_for, jsonify, request
from flask_bootstrap import Bootstrap5
from form import NewTodo
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String

app = Flask(__name__)
Bootstrap5(app)

# Secret Key for CSRF
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'sqlite:///to-do_list.db?timeout=10'  #This sets a 10-second timeout, allowing SQLite to wait before raising a locked error.
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class List(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    data_field: Mapped[str] = mapped_column(String, nullable=False)
    time_field: Mapped[str] = mapped_column(String, nullable=False)
    date_field: Mapped[str] = mapped_column(String, nullable=False)


#  Database Initialization (only run once)
# Ensure you run this once (maybe in a separate script or shell) to create your tables before inserting data:
# with app.app_context():
#     db.create_all()


@app.route("/")
def home():
    # READ ALL RECORDS
    # Construct a query to select from the database. Returns the rows in the database
    result = db.session.execute(db.select(List).order_by(List.data_field))
    # Use .scalars() to get the elements rather than entire rows from the database
    all_list = result.scalars().all()
    return render_template("index.html", to_list=all_list)


@app.route("/new-list", methods=['GET', 'POST'])
def new_todo():
    form = NewTodo()
    if form.validate_on_submit():
        formatted_date = form.date_field.data.strftime("%d-%m-%Y")
        print(type(
            formatted_date))  # This will print: 24-05-2025 strftime() function lets us convert a datetime object into a formatted string using special format codes.

        formatted_time = form.time_field.data.strftime("%H:%M")

        new_list = List(
            data_field=form.data_field.data,
            date_field=str(formatted_date),
            time_field=str(formatted_time)
        )

        db.session.add(new_list)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("form.html", form=form)


# @app.route("/<int:return_id>", methods=["POST"])
# def delete(return_id):
#     list_to_delete = db.session.execute(db.select(List).where(List.id == return_id)).scalar()
#     db.session.delete(list_to_delete)
#     db.session.commit()
#     flash("The list was deleted successfully!", "success")
#
#     return redirect(url_for("home"))

# Using AJAX(Asynchronous JavaScript and XML) Route to refresh
@app.route("/delete/<int:return_id>", methods=["POST"])
def delete(return_id):
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        list_to_delete = db.session.execute(db.select(List).where(List.id == return_id)).scalar()
        if list_to_delete:
            db.session.delete(list_to_delete)
            db.session.commit()
            return jsonify({"success": True})
        return jsonify({"success": False}), 404
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
