""" Results views """
from flask.views import MethodView

from app.api.service.result import office_result
from app.api.util.decorator import token_required


class ResultAPI(MethodView):
    """
    Office GET Results endpoint
    """

    @token_required
    def get(self, _id):
        # return the office results
        return office_result(office=_id)


# register ResultAPI class as view
results_view = ResultAPI.as_view('results')
