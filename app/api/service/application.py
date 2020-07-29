"""Methods for data manipulation between appplication
model and application endpoint
"""

from flask import jsonify, request
from marshmallow import ValidationError
from psycopg2 import IntegrityError


from app.api.util.dto import application_load_schema, application_dump_schema
from app.api.service.auth_helper import get_logged_in_user
from app.api.model.party import Party
from app.api.model.office import Office
from app.api.model.application import Application
from app.api.db.database import AppDatabase as db


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

    # decode the auth token of logged-in user
    res, status = get_logged_in_user(request)

    if status == 200:
        # get user id from decoded token
        applicant_id = res.get_json()['user'].get('user_id')

        party_id = get_party_id(party)
        office_id = get_office_id(office)

        if party_id and office_id:
            new_application = Application(
                party=party_id,
                office=office_id
            )

            try:
                save_changes(applicant_id, new_application)
            except IntegrityError:
                # Executed if the user has an application
                # already made before
                return jsonify({
                    "status": 400,
                    "error": "User has an application registered already."
                }), 400

            application_registered_query = Application.get_application(
                applicant_id)
            application_registered = db().get_single_row(*application_registered_query)
            response = application_dump_schema.dump(application_registered)

            response_object = jsonify({
                "status": 201,
                "data": [response]
            })
            return response_object, 201

        return jsonify({
            "status": 400,
            "error": "Party or office referenced does not exists."
        }), 400


def get_party_id(party_name):
    """gets id of the passed party name from the database

    Args:
        party_name (string): party name to query id for
    """
    party_name_query = Party.get_party_by_name(party_name)
    party = db().get_single_row(*party_name_query)
    if party:
        return party['id']


def get_office_id(office_name):
    """gets id of the passed office name from the database

    Args:
        office_name (string): office name oto query id for
    """
    office_name_query = Office.get_office_by_name(office_name)
    office = db().get_single_row(*office_name_query)
    if office:
        return office['id']


def save_changes(_id, data):
    """commit application details to the database

    Args:
        _id (integer): id of user making the application
        data (object): application instance
    """
    query, values = Application.add_application(data, user_id=_id)
    db().commit_changes(query, values)
