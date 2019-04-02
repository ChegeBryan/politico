"""petition view functions """

from flask import request, Blueprint
from flask.views import MethodView

from app.api.service.petition import save_new_petition
from app.api.util.decorator import token_required


petitions = Blueprint('petitions', __name__)


class PetitionsAPI(MethodView):
    """
    Party API endpoints
    """

    @token_required
    def post(self):
        # Create a new petition
        json_input = request.get_json()
        return save_new_petition(json_data=json_input)


# register the class as view
petitions_view = PetitionsAPI.as_view('petitions')

# api endpoints rules
petitions.add_url_rule(
    '/petitions', view_func=petitions_view, methods=["POST"])
