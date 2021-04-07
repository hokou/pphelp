from flask import Flask, redirect, render_template, session, url_for, request, jsonify
from markupsafe import escape
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from webmodel import User

app = Flask(__name__,
            static_folder="static",
            static_url_path="/")

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b"_5#y2LF4Q8z\n\xec]/"
# python -c 'import os; print(os.urandom(16))'

load_dotenv()
user_name = os.getenv("user_name")
password = os.getenv("password")
IP = os.getenv("IP")
db_name = os.getenv("db_name")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{user_name}:{password}@{IP}:3306/{db_name}"

db = SQLAlchemy(app)
# db.init_app(app)

error_code = {
    "1": "帳號或密碼錯誤",
    "2": "帳號已經被註冊",
    "3": "請註冊帳號",
    "4": "請重新登入"
}

@app.route("/")
def index():
    # print("index")
    if request.args.get('mess') != None:
        mess = request.args.get('mess')
    else:
        mess = ""
    return render_template("index.html",mess=mess)

@app.route("/signup", methods=["POST"])
def signup():
    if request.method == "POST":
        session.pop("mess", None)
        name = request.form["name_up"]
        username = request.form["usr_up"]
        password = request.form["pw_up"]
        query = User.query.filter_by(username=username).first()
        print("query",query)
        if query != None:
            message = error_code["2"]
            return redirect(url_for("error",message=message))
        else:
            signup_data = User(name=name, username=username, password=password)
            db.session.add(signup_data)
            db.session.commit()
            print("signup ok")
            mess = "註冊成功，請重新登入"
            return redirect(url_for("index",mess=mess))

@app.route("/signin", methods=["POST"])
def signin():
    if request.method == "POST":
        session.pop("mess", None)
        # sql_cmd = "select * from user where username="+"'"+request.form[f"usr_in"]+"'"+" and password="+"'"+request.form[f"pw_in"]+"'"+""
        # print("sqlcmd=",sql_cmd)
        # print(request.form[f"usr_in"],request.form[f"pw_in"])
        # query_data = db.engine.execute(sql_cmd)
        # print(query_data)
        username = request.form["usr_in"]
        password = request.form["pw_in"]
        query = User.query.filter_by(username=username).first()
        try:
            if query == None:
                error_message = error_code["3"]
                return redirect(url_for("error",message=error_message))
            elif username != query.username or password != query.password:
                error_message = error_code["1"]
                return redirect(url_for("error",message=error_message))
            elif username == query.username and password == query.password:
                session["username"] = username
                session["password"] = password
                session["name"] = query.name
                return redirect("/member")
        except:
            error_message = error_code["4"]
            return redirect(url_for("error",message=error_message))

@app.route("/signout", methods=["GET"])
def signout():
    session.pop("username", None)
    session.pop("password", None)
    session.pop("name", None)
    session.pop("mess", None)
    # print("signout del session")
    return redirect(url_for("index"))

@app.route("/member")
def member():
    session.pop("mess", None)
    if "username" and "password" in session:
        name = session["name"]
        # print("member")
        return render_template("member.html", name=name)
    else:
        # print("not signin")
        return redirect(url_for("signout"))

@app.route("/error/", methods=["GET"])
def error():
    error_message = request.args.get('message')
    print("error",error_message)
    return render_template("error.html",message=error_message)

@app.route("/api/users")
def api_users():
    username = request.args.get('username')
    query = User.query.filter_by(username=username).first()
    data = username_query(query)
    return jsonify(data)

def username_query(query):
    data = {"data":{}}
    if query != None:
        data["data"]["id"] = query.id
        data["data"]["name"] = query.name
        data["data"]["username"] = query.username
    elif query == None:
        data["data"] = None
    return data


if __name__ == "__name__":
    app.run(port=3000)

# == 語法查詢
# @app.route("/")
# def index():
#     sql_cmd = """
#     select * from user
#     """
#     query_data = db.engine.execute(sql_cmd)
#     print(query_data)
#     for x in query_data:
#         print(x)
#     return 'ok'