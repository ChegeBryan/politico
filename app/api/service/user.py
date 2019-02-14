""" Methods that involve data manipulation in the database """
from flask import jsonify
from marshmallow import ValidationError

from app.api.model.user import User
from app.api.util.dto import user_schema
from app.api.model.user import User
from app.api.db.database import AppDatabase, dsn

db = AppDatabase(dsn)

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
    password = data["password"]
    passportUrl = data["passportUrl"]
    isAdmin = data["isAdmin"]
    isPolitician = data["isPolitician"]

    new_user = User(firstname=firstname, lastname=lastname, othername=othername,email=email, phonenumber=phonenumber, password=password, passportUrl=passportUrl, isAdmin=isAdmin, isPolitician=isPolitician)

    save_changes(new_user)
    # 1. Serialize the input for response
    # 2. Return serialized and proper format json to api endpoint
    response = user_schema.dump(new_user)
    response_object = jsonify({
        "status": 201,
        "data": [response]
    })
    return response_object, 201

def get_user():
    """ Method to get the one single record from users relations. """
    pass

def get_all_users():
    """ Method to get all users in the users relations """
    pass

def save_changes(data):
    """ Write to the database """
    query, values = User.add_user(data)
    db.commit_changes(query, values)
