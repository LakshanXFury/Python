from flask import Flask, render_template
import requests


app = Flask(__name__)

response = requests.get("https://api.npoint.io/756b02afb8f0d5ae25e4")
post_response = response.json()


#Decorator
@app.route('/')
def home():
    print(post_response)

    return render_template("index.html", posts=post_response)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/blog/<int:index>')
def post_body(index):
    print(index)
    requested_post = None
    for blog_post in post_response:
        if blog_post["id"] == index:
            requested_post = blog_post
            print(f"This is the blog posst chosen{requested_post}")

    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)