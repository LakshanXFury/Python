from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/blog/<id>")
def get_blog(id):
    print(id)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts, blog_id=id)




if __name__ == "__main__":
    app.run(debug=True)