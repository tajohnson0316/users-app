from flask import session, render_template, request, redirect
from flask_app import app
from flask_app.models.user_model import User


@app.route("/")
def get_users():
    list_of_users = User.get_all()
    if len(list_of_users) == 0:
        return redirect("/user/form")
    return render_template("users.html", list_of_users=list_of_users)


@app.route("/users/form")
def display_user_form():
    return render_template("new-user-form.html")


@app.route("/users/new", methods=["POST"])
def create_user():
    print(request.form)
    new_user = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
    }

    user_id = User.create_one(new_user)
    return redirect("/")


@app.route("/users/<int:id>")
def display_user(id):
    data = {"id": id}
    user = User.get_one(data)
    return render_template("display-user.html", user=user)
