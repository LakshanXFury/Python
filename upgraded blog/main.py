from flask import Flask, render_template, request
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
            print(f"This is the blog post chosen{requested_post}")

    return render_template("post.html", post=requested_post)

@app.route("/form-entry", methods=["post"])
def receive_data():
    print(request.method)   # To check which method triggered the route.
    name = request.form["username"]
    email = request.form["email"]
    phone = request.form["email"]
    message = request.form["email"]
    print(f"Name:{name}\n Email:{email}\n Phone: {phone}\n Message: {message}")
    return f"<h1>Successfully sent your message {name}</h1>"


if __name__ == "__main__":
    app.run(debug=True)