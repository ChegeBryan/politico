# error handlers for the app.
from flask import jsonify


def method_not_allowed(e):
    """
    Json response for Method Not Allowed.
    """
    return jsonify({
        "status": 405,
        "error": "Method Not Allowed on Url."
    }), 405


def internal_server_error(e):
    """
    custom json response when server hits a 500
    """
    return jsonify({
        "status": 500,
        "error": "Our developers are looking into the issue."
    }), 500


def bad_request(e):
    """
    Custom json response for bad request at app level
    """
    return jsonify({
        "status": 400,
        "error": "Check your request format."
    }), 400


def url_not_found(e):
    """
    Custom json response for bad request at app level
    """
    return jsonify({
        "status": 404,
        "error": "Check url and try again."
    }), 404
