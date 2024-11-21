from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)
age_url = "https://api.agify.io?"


#Decorator
@app.route('/')
def server():
    year = datetime.datetime.now().year

    random_num = random.randint(1,100)

    return render_template("index.html", num=random_num, year=year)

#URL Building
@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts, blog_id=num)



if __name__ == "__main__":
    app.run(debug=True)