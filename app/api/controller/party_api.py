from flask import request, Blueprint
from flask.views import MethodView

from app.api.service.party import save_new_party

parties = Blueprint('parties', __name__)


class PartiesAPI(MethodView):
    """
    Party API endpoints
    """
    def post(self):
        # Create a new user
        json_input = request.get_json()
        return save_new_party(json_data=json_input)


# register the class as view
parties_view = PartiesAPI.as_view('parties')

# api endpoints rules
parties.add_url_rule('/parties', view_func=parties_view , methods=["POST"])
