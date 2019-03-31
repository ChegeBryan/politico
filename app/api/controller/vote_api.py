""" votes view """

from flask import request, Blueprint
from flask.views import MethodView

from app.api.service.vote import save_new_vote
from app.api.util.decorator import token_required


votes = Blueprint('votes', __name__)


class VoteAPI(MethodView):
    """ Vote method views """

    @token_required
    def post(self):
        json_input = request.get_json()
        return save_new_vote(json_data=json_input)


# register the class as view
votes_view = VoteAPI.as_view('votes')

votes.add_url_rule('/votes', view_func=votes_view, methods=["POST"])
