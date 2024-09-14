# Driver File (Brains)
from flask import Flask, request, sessions, redirect, session, g, Response, flash
from apis.users import users_api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(users_api)


@app.route("/", methods=['GET', 'POST'])
def index():
    return "hello world"


if __name__ == "__main__":
    app.run(debug=True)
