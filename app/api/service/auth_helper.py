""" User authentication helper methods """
from flask import jsonify
from marshmallow import ValidationError

from app.api.model.user import User
from app.api.db.database import AppDatabase as db
from app.api.util.dto import auth_schema, user_schema


def login_user(json_data):
    """Method checks if the user data provided is valid for login

    Args:
        data (json): User email and password
    """
    try:
        data = auth_schema.load(json_data)
    except ValidationError as e:
        return jsonify({
            "status": 400,
            "error": e.messages
        }), 400
    email = data["email"]

    # Query database for if provided user with email exists
    user_by_email = User.get_user_by_email(email)
    user_email = db().get_single_row(*user_by_email)
    if user_email:
        # check if password provided matches
        password_candidate = data['password']
        user_password = user_email['password']
        if User.verify_hash_password(password_candidate, user_password):
            access_token = User.encode_auth_token(email)
            response = user_schema.dump(user_email)
            return jsonify({
                "status": 200,
                "message": "Successfully logged in.",
                "data": [{
                    "token": access_token.decode(),
                    "user": [response]
                }]
            }), 200
        else:
            return jsonify({
                "status": 400,
                "error": "Incorrect user email or password."
            }), 400
    else:
        # when no user with particular email exists
        return jsonify({
            "status": 404,
            "message": "User does not exists."
        }), 404







