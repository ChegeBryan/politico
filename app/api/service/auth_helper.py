""" User authentication helper methods """
from flask import jsonify
from marshmallow import ValidationError

from app.api.model.user import User
from app.api.model.blacklist import BlacklistToken
from app.api.db.database import AppDatabase as db
from app.api.util.dto import auth_schema, user_schema
from app.api.service.blacklist import save_token


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


def logout_user(data):
    """Method to logout a user

    Args:
        data str: jwt token
    """
    if data:
        # get the token value from the "bearer and token" authorization string
        auth_token = data.split(" ")[1]
    else:
        """ if auth token is not available assign auth_token variable to
            an empty string
        """
        auth_token = ''
    if auth_token:
        """ decode the auth token if the result is not a valid email jump
            to the except section and return the error returned during
            token decoding
        """
        blacklisted_query = BlacklistToken.check_blacklist(auth_token)
        is_blacklisted = db().get_single_row(*blacklisted_query)
        if is_blacklisted is None:
            response = User.decode_auth_token(auth_token)
            try:
                auth_schema.load({'email': response}, partial=True)
                return save_token(auth_token)
            except ValidationError:
                """ expected response value:
                Expired token: "Signature expired. PLease login again."
                Invalid token: "Invalid token. PLease login again."
                """
                response_object = jsonify({
                    "status": 400,
                    "error": response
                })
                return response_object, 400
        else:
            response_object = jsonify({
                "status": 401,
                "error": "User is logged out, Please log in again."
            })
        return response_object, 401
    else:
        response_object = jsonify({
            "status": 403,
            "message": "Please provide a valid token."
        })
        return response_object, 403


def get_logged_in_user(request_header):
    # from the request get the authorization header
    auth_header = request_header.headers.get('Authorization')

    if auth_header:
        try:
            # check if the Authorization follows the format 'Bearer token-value'
            auth_token = auth_header.split(" ")[1]
        except IndexError:
            # when no token value can be established from the Authorization
            # value
            response_object = jsonify({
                'status': 401,
                'message': 'Malformed token. Check the token format.'
            })
            return response_object, 401
    else:
        auth_token = ''

    if auth_token:
        response = User.decode_auth_token(auth_token)
        try:
            # validate the response is an email
            auth_schema.load({'email': response}, partial=True)
            # get user with the response email from the database
            user_by_email = User.get_user_by_email(response)
            user = db().get_single_row(*user_by_email)
            response_object = jsonify({
                'status': 200,
                'user': {
                    'user_email': user['email'],
                    'is_admin': user['isadmin']
                }
            })
            return response_object, 200
        except ValidationError:
            """ expected response value:
            Expired token: "Signature expired. PLease login again."
            Invalid token: "Invalid token. PLease login again."
            """
            response_object = jsonify({
                "status": 401,
                "error": response
            })
            return response_object, 401
    else:
        response_object = jsonify({
            'status': 401,
            'message': 'Provide a valid auth token.'
        })
        return response_object, 401
