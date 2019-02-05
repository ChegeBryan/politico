from flask import request
from flask.views import MethodView

from app.api.service.party import save_new_party


class PartiesAPI(MethodView):
    """
    Party API endpoints
    """
    def post(self):
        # Create a new user
        json_input = request.get_json()
        return save_new_party(json_data=json_input)
