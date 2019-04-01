""" data manipulation  database and view """

from flask import jsonify

from app.api.model.result import get_office_result
from app.api.util.dto import results_schema
from app.api.db.database import AppDatabase as db


def office_result(office):
    """get the result set from the database

    Args:
        office (integer): the office to get results for
    """
    # sql query to get a user results
    results_query = get_office_result(office)
    office_result = db().get_all_rows(results_query)

    # serialize office results
    serialize_results = results_schema.dump(office_result)

    # json results response
    response_object = jsonify({
        "status": 200,
        "data": serialize_results
    })
    return response_object, 200
