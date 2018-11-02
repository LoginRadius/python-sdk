from user import user
from auth import auth
from flask import Flask, redirect

app = Flask(__name__)
app.register_blueprint(auth)
app.register_blueprint(user)

@app.route("/")
def main():
    return redirect("/loginscreen")

if __name__ == "__main__":
    app.run()