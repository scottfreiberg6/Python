from flask_app import app
from flask import render_template, request, redirect,session,flash
from flask_app.models.user import User
from flask_app.models.car import Car


@app.route("/car/new")
def new_car():
    if 'user_id' not in session:
        flash ("Please login or register before proceeding!")
        return redirect("/")
    return render_template ("new_car.html")

@app.route("/car/create", methods=["POST"])
def create_car():
    print('hello')
    # validate form info
    # if not Car.validate_car(request.form):
        # return redirect("/car/new")
        # Query Data
    print ('hello2')
    query_data= {
        "color": request.form["color"],
        "num_of_seats": request.form["num_of_seats"],
        "user_id":session["user_id"]
        }
        # Query using the data
    Car.create_car(query_data)
    print('hello3')
    return redirect("/dashboard")

@app.route("/car/show/<int:car_id>")
def show_car(car_id):
    if 'user_id' not in session:
        flash ("Please login or register before proceeding!")
        return redirect("/")
    query_data= {
        "car_id": car_id
    }
    car = Car.get_one_car(query_data)
    return render_template("show_car.html", one_car= car)
@app.route("/car/edit/<int:car_id>")
def edit_car(car_id):
    if 'user_id' not in session:
        flash ("Please login or register before proceeding!")
        return redirect("/")
    query_data= {
        "car_id": car_id
    }
    car = Car.get_one_car(query_data)
    return render_template("edit_car.html", one_car=car)
@app.route ("/car/update/<int:car_id>", methods=["post"])
def update_car(car_id):
    # if not Car.validate_car(request.form):
    #     return redirect(f"/car/edit/{id}")
    query_data = {
        "color": request.form["color"],
        "num_of_seats": request.form["num_of_seats"],
        "car_id": car_id
    }
    Car.update_car(query_data)
    return redirect("/dashboard")
@app.route("/car/delete/<int:car_id>")
def delete_car(car_id):
    query_data ={
    "car_id": car_id
}
    Car.delete_car(query_data)

    return redirect("/dashboard")



