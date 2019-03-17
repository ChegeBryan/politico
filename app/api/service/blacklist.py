""" Method to write to the blacklist table """

from flask import jsonify

from app.api.model.blacklist import BlacklistToken
from app.api.db.database import AppDatabase as db


def save_token(token):
    """ Method to save a token to the blacklist table when user logouts """
    blacklist_token = BlacklistToken(token)
    # insert the token to blacklist table
    query, values = BlacklistToken.add_blacklist_token(blacklist_token)
    db().commit_changes(query, values)
    response_object = jsonify({
        "status": 200,
        "message": "Successfully logged out."
    })
    return response_object, 200
