from flask import Flask, render_template
import random
import datetime

app = Flask(__name__)
age_url = "https://api.agify.io?"


#Decorator
@app.route('/')
def server():
    year = datetime.datetime.now().year

    random_num = random.randint(1,100)

    return render_template("index.html", num=random_num, year=year)



if __name__ == "__main__":
    app.run(debug=True)