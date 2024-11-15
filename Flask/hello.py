from flask import Flask

app = Flask(__name__)
print(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

# Decorator Fn
@app.route("/bye")
def bye():
    return "Bye Nibba..!!"

if __name__ == "__main__":
    app.run()
