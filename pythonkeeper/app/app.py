from flask import Flask

pythonkeeper = Flask(__name__)


@pythonkeeper.route("/register")
def register(username, password, email):
    return "ABC"


@pythonkeeper.route("/login")
def login(usernameOrEmail, password):
    return "DEF"
