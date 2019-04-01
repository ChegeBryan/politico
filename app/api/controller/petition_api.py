"""petition view functions """

from flask import request
from flask.views import MethodView

from app.api.service.petition import save_new_petition
from app.api.util.decorator import token_required


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
