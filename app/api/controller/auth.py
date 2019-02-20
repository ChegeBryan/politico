""" Login and logout controller endpoints """
from flask import request, Blueprint
from flask.views import MethodView

from app.api.service.auth_helper import login_user

auth = Blueprint(__name__, 'auth')


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

# register UserAuthAPI as view
auth_view = UserAuthAPI.as_view("auth")
auth.add_url_rule('/auth/signin', view_func=auth_view, methods=['POST'])
