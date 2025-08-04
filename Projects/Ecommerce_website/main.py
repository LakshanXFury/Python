from flask import Flask, request, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
Bootstrap5(app)


@app.route("/")
def home():
    pass


if __name__ == "__main__":
    app.run(debug=True)
