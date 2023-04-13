from flask import session, render_template, request, redirect
from flask_app import app
from flask_app.models.user_model import User


@app.route("/")
def get_users():
    list_of_users = User.get_all()
    if len(list_of_users) == 0:
        return redirect("/users/form")
    return render_template("users.html", list_of_users=list_of_users)


@app.route("/users/<int:id>")
def display_user(id):
    data = {"id": id}
    user = User.get_one(data)
    return render_template("display-user.html", user=user)


@app.route("/users/form")
def display_user_form():
    return render_template("new-user-form.html")


@app.route("/users/<int:id>/edit")
def display_user_edit_form(id):
    data = {"id": id}
    user = User.get_one(data)
    return render_template("edit-user-form.html", user=user)


@app.route("/users/new", methods=["POST"])
def create_user():
    print(request.form)
    new_user = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
    }

    user_id = User.create_one(new_user)
    return redirect(f"/users/{user_id}")


@app.route("/users/update/<int:id>", methods=["POST"])
def update_user(id):
    print(request.form)
    updated_user = {
        "id": id,
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
    }

    User.update_one(updated_user)
    return redirect(f"/users/{id}")


@app.route("/users/delete/<int:id>", methods=["POST"])
def delete_user(id):
    User.delete_one({"id": id})
    return redirect("/")
