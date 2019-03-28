"""  views """
from flask import request
from flask.views import MethodView

from app.api.service.candidate import save_new_candidate
from app.api.util.decorator import admin_token_required


class CandidateAPI(MethodView):
    """ Candidate method views """

    @admin_token_required
    def post(self, _id):
        # register candidate for office
        json_input = request.get_json()
        return save_new_candidate(office_id=_id, json_data=json_input)


# register the class as view
candidates_view = CandidateAPI.as_view('candidates')
