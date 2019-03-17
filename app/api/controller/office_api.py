""" Office views """
from flask import request, Blueprint
from flask.views import MethodView

from app.api.service.office import save_new_office, get_office, get_offices

offices = Blueprint('offices', __name__)


class OfficeAPI(MethodView):
    """
    Office POST, GET endpoints
    """

    def post(self):
        # create new office
        json_input = request.get_json()
        return save_new_office(json_data=json_input)

    def get(self, _id):
        if _id is None:
            # return list of all offices
            return get_offices()
        else:
            # return single offices
            return get_office(_id=_id)


# register officeAPI class as views
offices_view = OfficeAPI.as_view('offices')

# office endpoints rules
offices.add_url_rule('/offices', view_func=offices_view, methods=["POST"])
offices.add_url_rule('/offices/<uuid:_id>',
                     view_func=offices_view, methods=["GET"])
offices.add_url_rule('/offices', defaults={'_id': None},
                     view_func=offices_view, methods=["GET"])
