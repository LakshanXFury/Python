from flask import Flask, request, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)
Bootstrap5(app)
load_dotenv()  # This loads variables from the .env file

base_url = "https://api.marketstack.com/v1/eod"
ACCESS_KEY = os.getenv("API_ACCESS_KEY")


@app.route("/", methods=["GET"])
def home():
    stock_symbol = request.args.get("stock")  # It is getting from the name attribute in FORM
    if stock_symbol:
        return redirect(url_for('get_stock_data', stock_symbol=stock_symbol.upper()))
    return render_template("index.html", stock_data=None)


@app.route("/<stock_symbol>")
def get_stock_data(stock_symbol):
    upper_stock_symbol = stock_symbol.upper()
    print("User entered:", upper_stock_symbol)

    stock_params = {
        "access_key": ACCESS_KEY,
        "symbols": upper_stock_symbol
    }
    response = requests.get(base_url, params=stock_params)
    request_post = response.json()
    # Get the yesterday /recent data
    recent_data = request_post["data"][0]
    print(recent_data)

    if response.status_code == 200:
        if request_post:
            stock_info = recent_data
            return render_template("index.html", stock_data=stock_info, stock_symbol=stock_symbol)
        else:
            return render_template("index.html", stock_data=None, stock_symbol=stock_symbol)
    else:
        return f"Api Error : {response.status_code}"


if __name__ == "__main__":
    app.run(debug=True)
