from auth import auth
from flask import Flask, redirect
from user import user

app = Flask(__name__)
app.register_blueprint(auth)
app.register_blueprint(user)


@app.route("/")
def main():
    return redirect("/minimal")


if __name__ == "__main__":
    app.run()
