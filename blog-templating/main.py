from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/blog')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    blog_response = response.json()
    return render_template("index.html", posts=blog_response)


#URL Building
@app.route("/blog/<id>")
def get_blog_id(id):
    print(id)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    blog_response = response.json()
    return render_template("post.html", posts=blog_response, id=int(id))




if __name__ == "__main__":
    app.run(debug=True)
