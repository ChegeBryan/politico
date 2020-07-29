""" Login and logout controller endpoints """
from flask import request, Blueprint
from flask.views import MethodView

from app.api.service.auth_helper import login_user, logout_user

auth = Blueprint('auth', __name__)


class UserLoginAPI(MethodView):
    """
    User login
    """
    def post(self):
        """
        User login endpoint
        """
        json_input = request.get_json()
        return login_user(json_data=json_input)


class UserLogoutAPI(MethodView):
    """ User logout """
    def post(self):
        """ user logout endpoint """
        auth_header = request.headers.get('Authorization')
        return logout_user(data=auth_header)


# 1. register UserLoginAPI view
# 2. register UserLogoutAPI view
login_view = UserLoginAPI.as_view("user_login")
logout_view = UserLogoutAPI.as_view("user_logout")

auth.add_url_rule('/auth/signin', view_func=login_view, methods=['POST'])
auth.add_url_rule('/auth/signout', view_func=logout_view, methods=['POST'])
