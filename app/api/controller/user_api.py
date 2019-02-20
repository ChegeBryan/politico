from flask import request, Blueprint
from flask.views import MethodView

from app.api.service.user import save_new_user

users = Blueprint('users', __name__)

class UserRegistrationAPI(MethodView):
    """
    User registration
    """
    def post(self):
        """
        User Registration endpoint
        """
        json_input = request.get_json()
        return save_new_user(json_data=json_input)


# register the class as view
users_view = UserRegistrationAPI.as_view('users')

# api endpoints rules
users.add_url_rule('/auth/signup', view_func=users_view, methods=['POST'])

