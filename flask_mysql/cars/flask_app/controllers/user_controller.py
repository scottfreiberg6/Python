from flask_app import app
from flask import render_template, request, redirect,session,flash
from flask_app.models.user import User
from flask_app.models.car import Car
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)
@app.route ("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=['post'])
def register():
    if not User.validate_register(request.form):
        return redirect("/")

    pw_hash=bcrypt.generate_password_hash(request.form["password"])

    query_data={
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": pw_hash
    }

    new_user_id=User.register_user(query_data)

    session['user_id']=new_user_id

    return redirect("/dashboard")

@app.route("/login", methods=["post"])
def login():
    user=User.get_by_email(request.form)
    if not user:
        flash("Invalid email/password")
        return redirect("/")
    session["user_id"]=user.id        
    return redirect("/dashboard")

@app.route ("/dashboard")
def dashboard():
    if 'user_id' not in session:
        flash ("Please login or register before proceeding!")
        return redirect("/")

    query_data = {
        "user_id": session["user_id"]
    }
    all_cars=Car.get_all_cars()
    user=User.get_by_id(query_data)
    return render_template("dashboard.html", user=user, all_cars=all_cars)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

