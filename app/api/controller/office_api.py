""" Office views """
from flask import request, Blueprint
from flask.views import MethodView

from app.api.service.office import save_new_office

offices = Blueprint('office', __name__)

class OfficeAPI(MethodView):
    """
    Office POST, GET endpoints
    """
    def post(self):
        # create new office
        json_input = request.get_json()
        return save_new_office(json_data=json_input)
