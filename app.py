from flask import Flask, render_template, request, redirect, session
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash 
from helpers import apology, login_required
from datetime import datetime
from cs50 import SQL

app = Flask(__name__)


#config session to use filesyste(instead of signed cookies)
app.config["SESSION_PERMANENT"]="false"
app.config["SESSION_TYPE"]="filesystem"
Session(app)


db = SQL("sqlite:///database.db")

@app.route("/")
@login_required
def helloworld():
    return redirect("/dashboard")

@app.route("/register", methods = ["GET", "POST"])
def register():

    if request.method == "POST":
        #sajsbdja
        
        #ensure username was submitted
        if not request.form.get("username"):
            return apology("enter a username")
        #ensure password was submitted
        elif not request.form.get("password"):
            if not request.form.get("confirmation"):
                return apology("must provide password")
        #return apology if confirmation and password do not match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords do not match")
        
        #ensure same username does not exist
        users=db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        if len(users) == 1:
            return apology("username not available")
        else:
            #insert user credentials into the database
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", request.form.get("username"), generate_password_hash(request.form.get("password")))        


        return redirect("/login")
    else:
        return render_template("register.html")
        
@app.route("/login", methods=["GET", "POST"])
def login():

    session.clear()

    if request.method == "POST":
        #ensure if username was submitted
        if not request.form.get("username"):
            return apology("must provide username")
        #ensure if password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")
        
        #ensure username exists and password is correct
        row=db.execute("SELECT * FROM users WHERE username=?", request.form.get("username"))

        if len(row) != 1 or not check_password_hash(row[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password")
        
        #remember which user has logged in
        session["user_id"]=row[0]["id"]
        session["username"]=row[0]["username"]

        return redirect("/dashboard")
    else:
        return render_template("login.html")
    

@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    if request.method=="POST":

        return render_template("dashboard01.html", username=session["username"], )
    else:
        return render_template("dashboard01.html", username=session["username"], messages=db.execute("SELECT * FROM posts"))


@app.route("/send", methods=["POST"])
@login_required
def send():
    db.execute("INSERT INTO posts (id, post, uploaded, username) VALUES (?, ?, ?, ?)", session["user_id"], request.form.get("message"), datetime.now(), session["username"])
    return redirect("/dashboard")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")