from flask import Flask

app = Flask(__name__)
print(__name__)

@app.route("/")
def hello_world():
    return ('<h1 style="text-align: center; color:Tomato;">AOT</h1>'
            '<p> <b> Attack On Titan </b> </p>'
            '<img src = "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGxybnZ2amlhY2d1eTRtNHVmMWQwbzEyeDY0YXhzNWNrMzdoa'
            '2I3byZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l0Iyoy5VglR6QKJiw/giphy.gif">')

# Decorator Fn
@app.route("/bye")
def bye():
    return "Bye Nibba..!!"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old..!!!"



if __name__ == "__main__":
    app.run(debug=True)
