from flask import Flask, render_template
from flask_bootstrap import Bootstrap5



app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/robot-framework')
def testing():
    return render_template("testing.html")



if __name__ == '__main__':
    app.run(debug=True)