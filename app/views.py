from flask import Blueprint, request
from app.models import User

user = Blueprint("users", __name__)


@user.route("/register", methods=["POST"])
def register():
    data = request.form
    existing_user = User.get_by_email(data["email"])
    if existing_user:
        return {"message": "User already exist"}, 409
    User(**data).save()
    return {"message": "User registered Successfully"}, 201


@user.route("/login", methods=["POST"])
def login():
    data = request.form
    existing_user = User.get_by_email(data["email"])
    if not existing_user:
        return {"message": "Email doesnot exist"}, 404
    if not existing_user.authenticate(data["password"]):
        return {"message": "Password is incorrect"}, 403
    return {"message": "validation successful"}, 200
