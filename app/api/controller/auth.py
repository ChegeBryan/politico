""" Login and logout controller endpoints """
from flask import request
from flask.views import MethodView

from app.api.controller.user_api import users
from app.api.service.auth_helper import login_user


class UserAuthAPI(MethodView):
    """
    User login
    """
    def post(self):
        """
        User login endpoint
        """
        json_input = request.get_json()
        return login_user(json_data=json_input)

