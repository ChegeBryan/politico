""" Application views """
from flask import request, Blueprint
from flask.views import MethodView


from app.api.service.application import save_new_application
from app.api.util.decorator import token_required


application = Blueprint('application', __name__)


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

# application endpoint rules
application.add_url_rule('/office/application',
                         view_func=application_view, methods=['POST'])
