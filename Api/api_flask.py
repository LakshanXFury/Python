from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Home"


#Get Route

@app.route("/get-user/<user_id>")  # Path parameter
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "Lakshan S",
        "email": "lakshan@gmail.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200


#Post Route
@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data), 201


if __name__ == "__main__":
    app.run(debug=True)
