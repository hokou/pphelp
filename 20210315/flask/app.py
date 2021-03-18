from flask import Flask, redirect, render_template, session, url_for, request
from markupsafe import escape

app = Flask(__name__,
            static_folder="static",
            static_url_path="/")

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b"_5#y2LF4Q8z\n\xec]/"

name_ans ="test"
password_ans = "test"

@app.route("/")
def index():
    # print("index")
    return render_template("index.html")

@app.route("/signin", methods=["POST"])
def signin():
    if request.method == "POST":
        name = request.form["usr"]
        password = request.form["pw"]
        if name == name_ans and password == password_ans:
            session["username"] = name
            session["password"] = password
            # print("save session")
            return redirect("/member")
        else:
            # print("no save session")
            return redirect("/error")

@app.route("/signout", methods=["GET"])
def signout():
    session.pop("username", None)
    session.pop("password", None)
    # print("signout del session")
    return redirect(url_for("index"))

@app.route("/member")
def member():
    if "username" and "password" in session:
        name = session["username"]
        # print("member")
        return render_template("member.html", user=name)
    else:
        # print("not signin")
        return redirect(url_for("signout"))

@app.route("/error")
def error():
    # print("error")
    return render_template("error.html")

if __name__ == "__name__":
    app.run(port=3000)