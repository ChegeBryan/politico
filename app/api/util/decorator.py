from functools import wraps
from flask import request


from app.api.service.auth_helper import get_logged_in_user


def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        # get the request body using flask request function as a variable
        data, status = get_logged_in_user(request)
        try:
            # verify data response dictionary contains the 'user' key
            data.get_json()['user']
        except KeyError:
            return data, status

        return func(*args, **kwargs)

    return decorated
