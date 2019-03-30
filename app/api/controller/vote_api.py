""" votes view """

from flask import request
from flask.views import MethodView

from app.api.service.vote import save_new_vote
from app.api.util.decorator import token_required


class VoteAPI(MethodView):
    """ Vote method views """

    @token_required
    def post(self):
        auth_header = request.headers.get('Authorization')
        json_input = request.get_json()
        return save_new_vote(token=auth_header, json_data=json_input)


# register the class as view
votes_view = VoteAPI.as_view('votes')


