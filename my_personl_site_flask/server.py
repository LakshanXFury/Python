from flask import Flask, render_template


app = Flask(__name__)



#Decorator
@app.route('/')
def server():
    return render_template("html5up.html")


if __name__ == "__main__":
    app.run(debug=True)