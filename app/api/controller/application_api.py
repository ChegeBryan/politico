""" Application views """
from flask import request
from flask.views import MethodView


from app.api.service.application import save_new_application
from app.api.util.decorator import token_required


class ApplicationApi(MethodView):
    """
    Application endpoint
    """

    @token_required
    def post(self):
        # register user office application
        json_input = request.get_json()
        return save_new_application(json_input)


# register application api class as a view
application_view = ApplicationApi.as_view('application')
