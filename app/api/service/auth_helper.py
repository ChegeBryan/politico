""" User authentication helper methods """
from flask import jsonify

from app.api.model.user import User
from app.api.db.database import AppDatabase as db
from app.api.util.dto import auth_schema, user_schema


def login_user(json_data):
    """Method checks if the user data provided is valid for login

    Args:
        data (json): User email and password
    """
    data = auth_schema.load(json_data)
    email = data["email"]

    # Query database for if provided user with email exists
    user_by_email = User.get_user_by_email(email)
    user_email = db().get_single_row(*user_by_email)
    if user_email:
        # check if password provided matches
        pass
    else:
        # when no user with particular email exists
        return jsonify({
            "status": 404,
            "message": "User does not exists."
        }), 404







