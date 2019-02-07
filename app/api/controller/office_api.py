""" Office views """
from flask import request
from flask.views import MethodView

from app.api.service.office import save_new_office

class OfficeAPI(MethodView):
    """
    Office POST, GET endpoints
    """
    def post(self):
        # create new office
        json_input = request.get_json()
        return save_new_office(json_data=json_input)
