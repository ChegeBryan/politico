""" Methods that involve data manipulation in the database """
from flask import jsonify
from marshmallow import ValidationError

from app.api.model.user import User
from app.api.util.dto import user_schema
from app.api.db.database import AppDatabase as db


def save_new_user(json_data):
    """ Method to save a new user to the database """

    # 1. Deserialize the data input against the user schema
    # 2. check for validation errors
    try:
        data = user_schema.load(json_data)
    except ValidationError as e:
        return jsonify({
            "status": 400,
            "error": e.messages
        }), 400
    firstname = data["firstname"]
    lastname = data["lastname"]
    othername = data["othername"]
    email = data["email"]
    phonenumber = data["phonenumber"]
    password = User.generate_hash_password(data["password"])
    passportUrl = data["passporturl"]
    isAdmin = data["isadmin"]
    isPolitician = data["ispolitician"]

    # 1. query database if provided email exists.
    # 2. if it exists exit with a 409 error
    user_by_email = User.get_user_by_email(email)
    user_by_passport = User.get_user_by_passport(passportUrl)
    user_email = db().get_single_row(*user_by_email)
    user_passport = db().get_single_row(*user_by_passport)
    if user_email is None and user_passport is None:
        new_user = User(firstname=firstname, lastname=lastname,
                        othername=othername, email=email,
                        phonenumber=phonenumber,
                        password=password, passportUrl=passportUrl,
                        isAdmin=isAdmin, isPolitician=isPolitician
                        )

        # save the user and return the id for that user
        returned_id = save_changes(new_user)
        # 1. Serialize the input for response
        # 2. Return serialized and proper format json to api endpoint
        access_token = new_user.encode_auth_token(returned_id)
        response = user_schema.dump(new_user)
        response_object = jsonify({
            "status": 201,
            "data": [{
                "token": access_token.decode(),
                "user": [response]
            }]
        })
        return response_object, 201

    # when none of the conditions are satisfied
    return jsonify({
        "status": 409,
        "error": "User with that email or passport exists."
    }), 409


def get_user():
    """ Method to get the one single record from users relations. """
    pass


def get_all_users():
    """ Method to get all users in the users relations """
    pass


def save_changes(data):
    """ Write to the database """
    query, values = User.add_user(data)
    identifier = db().commit_changes_returning_id(query, values)
    return identifier
