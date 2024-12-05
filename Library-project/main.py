from flask import Flask, render_template, request, redirect, url_for

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # Get form data from the user
        book_name = request.form["bookname"]
        book_author = request.form["bookauthor"]
        book_rating = request.form["rating"]

        # Append book details to the list
        all_books.append({
            "name": book_name,
            "author": book_author,
            "rating": book_rating
        })

        # Display all_books in the console for verification
        print(all_books)

        # Return a response showing successful addition (for now)
        # return f"Book added: {book_name}, {book_author}, {book_rating}"
        return redirect(url_for("home"))

    # Render the add.html form for GET requests
    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)

