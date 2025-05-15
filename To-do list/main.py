from flask import Flask, flash, render_template, redirect, url_for, abort
from flask_bootstrap import Bootstrap5
from form import NewTodo

app = Flask(__name__)
Bootstrap5(app)


@app.route("/")
def home():
    return render_template("index.html")


def new_todo():
    form = NewTodo()
    # if form.validate_on_submit():

    return render_template("form.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
