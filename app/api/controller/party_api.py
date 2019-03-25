from flask import request, Blueprint
from flask.views import MethodView

from app.api.service.party import (
    save_new_party, get_party, get_parties, edit_party, delete_party)
from app.api.util.decorator import admin_token_required, token_required

parties = Blueprint('parties', __name__)


class PartiesAPI(MethodView):
    """
    Party API endpoints
    """

    @admin_token_required
    def post(self):
        # Create a new user
        json_input = request.get_json()
        return save_new_party(json_data=json_input)

    @token_required
    def get(self, _id):
        if _id is None:
            # return list of all parties
            return get_parties()
        else:
            # return single party
            return get_party(_id=_id)

    @admin_token_required
    def patch(self, _id):
        # edit party details
        json_input = request.get_json()
        return edit_party(_id=_id, json_data=json_input)

    def delete(self, _id):
        # delete a political party
        return delete_party(_id=_id)


# register the class as view
parties_view = PartiesAPI.as_view('parties')

# api endpoints rules
parties.add_url_rule('/parties', view_func=parties_view, methods=["POST"])
parties.add_url_rule('/parties/<int:_id>',
                     view_func=parties_view, methods=["GET", "DELETE"])
parties.add_url_rule('/parties', defaults={'_id': None},
                     view_func=parties_view, methods=["GET"])
parties.add_url_rule('/parties/<uuid:_id>/name',
                     view_func=parties_view, methods=["PATCH"])
