"""Methods for data manipulation between appplication
model and application endpoint
"""

from flask import jsonify
from marshmallow import ValidationError


from app.api.util.dto import application_load_schema


def save_new_application(json_data):
    """Create a user office application instance and save the data to
    the database

    Args:
        json_data (json): office user is vying for and the party name
    """

    # deserialize the data input against the application schema
    # checks if the input values pass the field validation
    try:
        data = application_load_schema.load(json_data)
    except ValidationError as e:
        return jsonify({
            "status": 400,
            "error": e.messages
        }), 400
    party = data['party']
    office = data['office']
