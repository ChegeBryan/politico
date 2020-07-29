from functools import wraps
from flask import request, jsonify


from app.api.service.auth_helper import get_logged_in_user


def token_required(func):
    """decorator to check if the a valid token is provided to
    access an endpoint

    inner_function:
        @wraps(func): preserves identity of the initial function

    Args:
        func (function): reference to a endpoint method

    Returns:
        [json]: the decorator will return the decorated function return
         value or the errors encountered during token decoding
    """

    @wraps(func)
    def decorated(*args, **kwargs):
        # pass flask.request as an argument to the get_logged_in_user()
        data, status = get_logged_in_user(request)
        try:
            # verify data response dictionary contains the 'user' key
            data.get_json()['user']
        except KeyError:
            return data, status

        return func(*args, **kwargs)

    return decorated


def admin_token_required(func):
    """decorator to check if the valid token is provided to
    access an endpoint and the user token is associated with an admin user

    inner_function:
        @wraps(func): preserves identity of the initial function

    Args:
        func (function): reference to a endpoint method

    Returns:
        [json]: the decorator will return the decorated function return
         value or the errors encountered during token decoding
    """
    @wraps(func)
    def decorated(*args, **kwargs):
        # pass flask.request as an argument to the get_logged_in_user()
        data, status = get_logged_in_user(request)
        try:
            # verify data response dictionary contains the 'user' key
            data.get_json()['user']
            admin = data.get_json()['user'].get('is_admin')
            if not admin:
                # if the admin value is False
                response_object = jsonify({
                    'status': 401,
                    'message': 'Admin token required.'
                })
                return response_object, 401

        except KeyError:
            return data, status

        return func(*args, **kwargs)

    return decorated
