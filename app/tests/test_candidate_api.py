""" Tests for candidate registration endpoint """

from .base_test import BaseTestData

from app.api.db.user_test_data import user_2
from app.api.db.candidate_test_data import (null_party_id, null_candidate_id,
                                            candidate_string_value,
                                            party_string_value,
                                            missing_party_field,
                                            missing_candidate_field,
                                            candidate, duplicate_party_office)


class CandidateAPITestCases(BaseTestData):
    """ Test case class for candidate registration API """

    def test_candidate_registration(self):
        """Test api return the correct status code on success
        candidate registration
        : return STATUS CODE 201 Ok Created
        """
        response = self.register_candidate
        json_body = response.get_json()
        self.assertEqual(json_body["status"], 201)
        self.assertEqual(json_body["data"][0]["party"], 1)
        self.assertEqual(json_body["data"][0]["office"], 1)
        self.assertEqual(json_body["data"][0]["candidate"], 2)
        self.assertTrue(json_body["data"][0]["registered_on"])
        self.assertEqual(response.status_code, 201)

    def test_empty_party_id_value(self):
        """
        Test api returns correct error code and response message on attempt to
        register a candidate with missing data in party field
        : return STATUS CODE 400 Bad Request
        """
        # get token of signed in admin user
        auth_token = self.admin_token

        response = self.client.post(
            '/api/v2/office/1/register',
            json=null_party_id,
            headers={
                "Authorization": "Bearer {}".format(auth_token)
            }
        )
        json_data = response.get_json()
        self.assertEqual(json_data["status"], 400)
        self.assertEqual(json_data["error"]["party"][0],
                         "Not a valid integer.")
        self.assertEqual(response.status_code, 400)

    def test_empty_candidate_id_value(self):
        """
        Test api returns correct error code and response message on attempt to
        register a candidate with missing data in candidate field
        : return STATUS CODE 400 Bad Request
        """
        # get token of signed in admin user
        auth_token = self.admin_token

        response = self.client.post(
            '/api/v2/office/1/register',
            json=null_candidate_id,
            headers={
                "Authorization": "Bearer {}".format(auth_token)
            }
        )
        json_data = response.get_json()
        self.assertEqual(json_data["status"], 400)
        self.assertEqual(json_data["error"]["candidate"][0],
                         "Not a valid integer.")
        self.assertEqual(response.status_code, 400)

    def test_candidate_id_is_string_value(self):
        """
        Test api returns correct error code and response message on attempt to
        register a candidate with a string value as id in candidate field
        : return STATUS CODE 400 Bad Request
        """
        # get token of signed in admin user
        auth_token = self.admin_token

        response = self.client.post(
            '/api/v2/office/1/register',
            json=candidate_string_value,
            headers={
                "Authorization": "Bearer {}".format(auth_token)
            }
        )
        json_data = response.get_json()
        self.assertEqual(json_data["status"], 400)
        self.assertEqual(json_data["error"]["candidate"][0],
                         "Not a valid integer.")
        self.assertEqual(response.status_code, 400)

    def test_party_id_is_string_value(self):
        """
        Test api returns correct error code and response message on attempt to
        register a candidate with a string value as id in party field
        : return STATUS CODE 400 Bad Request
        """
        # get token of signed in admin user
        auth_token = self.admin_token

        response = self.client.post(
            '/api/v2/office/1/register',
            json=party_string_value,
            headers={
                "Authorization": "Bearer {}".format(auth_token)
            }
        )
        json_data = response.get_json()
        self.assertEqual(json_data["status"], 400)
        self.assertEqual(json_data["error"]["party"][0],
                         "Not a valid integer.")
        self.assertEqual(response.status_code, 400)

    def test_missing_party_field(self):
        """
        Test api returns correct error code and response message on attempt to
        register a candidate without a the required field (party)
        : return STATUS CODE 400 Bad Request
        """
        # get token of signed in admin user
        auth_token = self.admin_token

        response = self.client.post(
            '/api/v2/office/1/register',
            json=missing_party_field,
            headers={
                "Authorization": "Bearer {}".format(auth_token)
            }
        )
        json_data = response.get_json()
        self.assertEqual(json_data["status"], 400)
        self.assertEqual(json_data["error"]["party"][0],
                         "Missing data for required field.")
        self.assertEqual(response.status_code, 400)

    def test_missing_candidate_field(self):
        """
        Test api returns correct error code and response message on attempt to
        register a candidate without a the required field (candidate)
        : return STATUS CODE 400 Bad Request
        """
        # get token of signed in admin user
        auth_token = self.admin_token

        response = self.client.post(
            '/api/v2/office/1/register',
            json=missing_candidate_field,
            headers={
                "Authorization": "Bearer {}".format(auth_token)
            }
        )
        json_data = response.get_json()
        self.assertEqual(json_data["status"], 400)
        self.assertEqual(json_data["error"]["candidate"][0],
                         "Missing data for required field.")
        self.assertEqual(response.status_code, 400)

    def test_candidate_double_registration_on_same_office(self):
        """
        Test api returns correct error code and response message on attempt to
        register a candidate again on the same office
        : return STATUS CODE 409 Conflict
        """

        response = self.register_candidate
        self.assertEqual(response.status_code, 201)

        # get token of signed in admin user
        auth_token = self.admin_token

        response_2 = self.client.post(
            '/api/v2/office/1/register',
            json=candidate,
            headers={
                "Authorization": "Bearer {}".format(auth_token)
            }
        )
        json_data = response_2.get_json()
        self.assertEqual(json_data["status"], 409)
        self.assertEqual(json_data["error"], "Data conflicts encountered.")
        self.assertEqual(response_2.status_code, 409)

    def test_party_only_registers_once_for_an_office(self):
        """
        Test api returns correct error code and response message on attempt to
        register a candidate to an office that has a candidate from the same
        party registered
        : return STATUS CODE 409 Conflict
        """

        res_reg_candidate = self.register_candidate
        self.assertEqual(res_reg_candidate.status_code, 201)

        # register a new user
        res_signup_user = self.client.post(
            '/api/v2/auth/signup', json=user_2
        )
        self.assertEqual(res_signup_user.status_code, 201)

        # get token of signed in admin user
        auth_token = self.admin_token

        # register a new candidate to the same office under the same party
        res_reg_same_party = self.client.post(
            '/api/v2/office/1/register',
            json=duplicate_party_office,
            headers={
                "Authorization": "Bearer {}".format(auth_token)
            }
        )
        json_data = res_reg_same_party.get_json()
        self.assertEqual(json_data["status"], 409)
        self.assertEqual(json_data["error"], "Party already represented.")
        self.assertEqual(res_reg_same_party.status_code, 409)
