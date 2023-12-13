from flask import Flask, render_template, request, redirect, session, jsonify
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

db = SQL("sqlite:///database/database.db")

@app.route("/")
@login_required
def helloworld():
    return redirect("/dashboard")


@app.route("/register", methods = ["GET", "POST"])
def register():

    if request.method == "POST":
        
        if not request.form.get("username"):
            return apology("enter a username")
        
        elif not request.form.get("name"):
            return apology("enter a name")
        
        elif not request.form.get("password"):
            if not request.form.get("confirmation"):
                return apology("must provide password")
        
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords do not match")
        
        
        users=db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        if len(users) == 1:
            return apology("username not available")
        else:
            
            db.execute("INSERT INTO users (name, username, hash) VALUES (?, ?, ?)",request.form.get("name"), request.form.get("username"), generate_password_hash(request.form.get("password")))        


        return redirect("/login")
    else:
        return render_template("register.py.jinja")
        

@app.route("/login", methods=["GET", "POST"])
def login():

    session.clear()

    if request.method == "POST":
        
        if not request.form.get("username"):
            return apology("must provide username")
        
        elif not request.form.get("password"):
            return apology("must provide password")
        
        
        row=db.execute("SELECT * FROM users WHERE username=?", request.form.get("username"))

        if len(row) != 1 or not check_password_hash(row[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password")
        
    
        session["user_id"]=row[0]["id"]
        session["username"]=row[0]["username"]

        return redirect("/dashboard")
    else:
        return render_template("login.py.jinja.j2")
    


@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    if request.method=="POST":

        return render_template("dashboard01.py.jinja", username=session["username"], )
    else:
        print("asdasdasdasdasd")
        post_data = db.execute("SELECT * FROM posts")
        like = db.execute("SELECT * FROM likes WHERE user_id=?", session["user_id"])
        post_id=[]
        for i in like:
            post_id.append(i["post_id"])
        print(post_id)
        
        for i in post_data:
            if i["post_id"] in post_id:
                i.update({"post_liked": "1"})
            else:
                i.update({"post_liked": "0"})
            print(i)
        
        return render_template("dashboard01.py.jinja", post_data=post_data)


@app.route("/add", methods=["POST"])
@login_required
def add():
    print("sadasdasdasdascgabjgdsjashd")
    db.execute("INSERT INTO posts (username, post, post_time, name, likes) VALUES (?, ?, ?, ?, ?)", session["username"], request.form.get("message"), datetime.now(), db.execute("SELECT name FROM users WHERE username = ?", session["username"])[0]["name"], 0)
    return redirect("/dashboard")


@app.route("/likes", methods=["GET","POST"])
@login_required
def likes():

    liked = db.execute("SELECT * FROM likes WHERE user_id = ? AND post_id = ?", session["user_id"], request.args.get("post_id"))
    if not liked :
        db.execute("INSERT INTO likes (user_id, post_id) VALUES (?, ?)", session["user_id"], request.args.get("post_id"))
        
    db.execute("UPDATE posts SET likes = likes + 1 WHERE post_id = ?", request.args.get("post_id"))
    like_count = db.execute("SELECT likes FROM posts WHERE post_id = ?", request.args.get("post_id"))[0]["likes"]
    return str(like_count)


@app.route("/dislikes", methods=["GET", "POST"])
@login_required
def dislikes():
    db.execute("DELETE FROM likes WHERE user_id = ? AND post_id = ?", session["user_id"], request.args.get("post_id"))
    db.execute("UPDATE POSTS SET likes = likes - 1 WHERE post_id = ?", request.args.get("post_id"))

    like_count = db.execute("SELECT likes FROM posts WHERE post_id = ?", request.args.get("post_id"))[0]["likes"]
    return str(like_count)


@app.route("/liked_data", methods=["GET", "POST"])
@login_required
def liked_data():
    post_id = request.args.get("post_id")
    print(post_id)

    like_data = db.execute("SELECT * FROM likes WHERE user_id=? AND post_id = ?", session["user_id"], post_id)

    if not like_data:
        db.execute("UPDATE posts SET likes = likes + 1 WHERE post_id=?", post_id)
        db.execute("INSERT INTO likes (user_id, post_id) VALUES(?, ?)", session["user_id"], post_id)

        likes = db.execute("SELECT likes FROM posts WHERE post_id = ?", post_id)[0]["likes"]
        return f"like{likes}"
    else:
        db.execute("UPDATE posts SET likes = likes - 1 WHERE post_id=?", post_id)
        db.execute("DELETE FROM likes WHERE user_id = ? AND post_id = ?", session["user_id"], post_id)

        likes = db.execute("SELECT likes FROM posts WHERE post_id = ?", post_id)[0]["likes"]
        return f"dislike{likes}"


@app.route("/search", methods=["POST","GET"])
@login_required
def search():
    search_string=request.args.get("search")
    post_data = db.execute("SELECT * FROM posts WHERE post LIKE ? ", '%' + search_string + '%')

    like = db.execute("SELECT * FROM likes WHERE user_id=?", session["user_id"])
    post_id=[]
    for i in like:
        post_id.append(i["post_id"])
        print(post_id)
        
    for i in post_data:
        if i["post_id"] in post_id:
            i.update({"post_liked": "1"})
        else:
            i.update({"post_liked": "0"})
        print(i)
    return render_template("dashboard01.py.jinja", post_data=post_data)


@app.route("/sort", methods=["GET", "POST"])
@login_required
def sort():
    post_data = db.execute("SELECT * FROM posts")
    like = db.execute("SELECT * FROM likes WHERE user_id=?", session["user_id"])
    post_id=[]
    for i in like:
        post_id.append(i["post_id"])
    print(post_id)
    
    for i in post_data:
        if i["post_id"] in post_id:
            i.update({"post_liked": "1"})
        else:
            i.update({"post_liked": "0"})
    print(post_data)
    
    sort_by=request.args.get("sort_by")

    if sort_by=="liked" :
        new_post_data=sorted(post_data, key=lambda d: d['likes'], reverse=True)
    else:
        new_post_data=sorted(post_data, key=lambda d: d['likes'])

    return render_template("dashboard01.py.jinja", post_data=new_post_data)


@app.route("/viewposts", methods=["POST", "GET"])
@login_required
def viewpost():
    post_id=request.args.get("post_id")
    post = db.execute("SELECT * FROM posts WHERE post_id=?", post_id)
    liked = db.execute("SELECT * FROM likes WHERE user_id=? AND post_id=?", session["user_id"], post_id)
    reply=db.execute("SELECT * FROM comments WHERE post_id=?", post_id)

    for i in reply:
        i["name"]=db.execute("SELECT name FROM users WHERE id=?", i["user_id"])[0]["name"]
        i["username"]=db.execute("SELECT username FROM users WHERE id=?", i["user_id"])[0]["username"]

    print(reply)
    if not liked:
        count=0
    else:
        count=1
    print(count)
    return render_template("post.py.jinja", post=post, count=count, reply=reply)



@app.route("/comment", methods=["GET", "POST"])
@login_required
def comment():
    post_id=request.form.get("post_id")
    db.execute("INSERT INTO comments (post_id, comment, user_id, comment_time) VALUES (?, ?, ?, ?)", request.form.get("post_id"), request.form.get("comment"), session["user_id"], datetime.now())
    return redirect(f"/viewposts?post_id={post_id}")

@app.route("/myprofile", methods=["GET", "POST"])
@login_required
def myprofile():
    choice=request.args.get("myprofile")
    print(choice)
    if choice == "myposts":
        post_data = db.execute("SELECT * FROM posts WHERE username=?", session["username"])
        like = db.execute("SELECT * FROM likes WHERE user_id=?", session["user_id"])
        post_id=[]
        for i in like:
            post_id.append(i["post_id"])
        
        
        for i in post_data:
            if i["post_id"] in post_id:
                i.update({"post_liked": "1"})
            else:
                i.update({"post_liked": "0"})
        print(post_data)
        return render_template("myprofile.py.jinja", post_data=post_data)
    
    if choice == "likedposts":
        post_data = db.execute("SELECT * FROM posts")
        like = db.execute("SELECT * FROM likes WHERE user_id=?", session["user_id"])
        post_id=[]
        for i in like:
            post_id.append(i["post_id"])
        print(post_id)
        
        for i in post_data:
            if i["post_id"] in post_id:
                i.update({"post_liked": "1"})
            else:
                i.update({"post_liked": "0"})
        
        liked_post=[]
        for i in post_data:
            if i["post_liked"] == "1":
                liked_post.append(i)
    
        return render_template("myprofile.py.jinja", post_data=liked_post)
    if choice == "comments":
        comment_data = db.execute("SELECT * FROM comments WHERE user_id=?", session["user_id"])
        user_data=db.execute("SELECT name, username FROM users WHERE id=?", session["user_id"])[0]

        return render_template("myprofile.py.jinja", comment_data=comment_data, username=user_data["username"], name=user_data["name"])
    return render_template("myprofile.py.jinja")

@app.route("/delete", methods=["GET", "POST"])
@login_required
def delete():
    choice=request.args.get("id")
    if choice[0:3] == "cmt":
        db.execute("DELETE FROM comments WHERE comment_id=?", choice[3:])
    else:
        db.execute("DELETE FROM posts WHERE post_id=?", choice[4:])
    
    print(choice)
    return "delete"

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")