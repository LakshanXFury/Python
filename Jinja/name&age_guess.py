from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/guess/<name>")
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    actual_gender = gender_response.json()["gender"]

    age_url = f"https://api.agify.io/?name={name}"
    age_response = requests.get(age_url)
    actual_age = age_response.json()["age"]

    return render_template("name&age.html", person_name=name, gender=actual_gender, old=actual_age)









if __name__ == "__main__":
    app.run(debug=True)


