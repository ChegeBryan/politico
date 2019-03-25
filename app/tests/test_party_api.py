""" Tests for party api endpoints """
import uuid

from .base_test import BaseTestData
from app.api.db.party_test_data import (
    null_party_entries_holder, null_party_hq_holder,
    int_party_name_holder, null_party_name_holder, party_holder)


class PartyAPITestCase(BaseTestData):
    """
    Class for testing api methods
    """

    def test_create_party(self):
        """
        Test api return correct status code on success
        : return STATUS CODE 201 Ok Created
        """

        #  app testing client
        response = self.post_data
        json_body = response.get_json()
        self.assertIsInstance(json_body["data"], list)
        self.assertEqual(response.status_code, 201)

    def test_party_route_protection_no_authorization_header(self):
        """
        Test API return authorization error when no header is provided when
        accessing parties route for with post method
        : return STATUS CODE 401 Unauthorized
        """
        response = self.client.post(
            '/api/v2/parties', json=party_holder
        )
        json_data = response.get_json()
        self.assertEqual(json_data["message"], "Provide a valid auth token.")
        self.assertEqual(response.status_code, 401)

    def test_party_route_protection_normal_user_authorization_header(self):
        """
        Test API return authorization error when authorization header
        provided is a normal user token when accessing parties route for with
        post method
        : return STATUS CODE 401 Unauthorized
        """
        # register a user
        signup = self.user_data
        self.assertEqual(signup.status_code, 201)

        # login registered user
        signin = self.login_data
        json_body = signin.get_json()
        auth_token = json_body["data"][0]["token"]
        self.assertTrue(signin.status_code, 200)

        response = self.client.post(
            '/api/v2/parties', json=party_holder, headers={
                "Authorization": "Bearer {}".format(auth_token)}
        )
        json_data = response.get_json()
        self.assertEqual(json_data["message"], "Admin token required.")
        self.assertEqual(response.status_code, 401)

    def test_party_route_protection_malformed_authorization_header(self):
        """
        Test API return authorization error when authorization header
        provided is malformed
        : return STATUS CODE 401 Unauthorized
        """
        response = self.client.post(
            '/api/v2/parties', json=party_holder, headers={
                "Authorization": "Bearer qwwme.amsms.wnsm"}
        )
        json_data = response.get_json()
        self.assertEqual(
            json_data["error"], "Invalid token. PLease login again."
            )
        self.assertEqual(response.status_code, 401)

    def test_party_route_protection_admin_logged_out(self):
        """
        Test API return authorization error when authorization header
        provided is the is blacklisted. admin is logged out
        : return STATUS CODE 401 Unauthorized
        """
        admin_signin = self.admin_signin
        auth_token = self.admin_token
        admin_signout = self.client.post(
            '/api/v2/auth/signout', headers={
                "Authorization": "Bearer {}".format(self.admin_token)}
        )
        json_body = admin_signout.get_json()
        self.assertEqual(json_body["status"], 200)

        response = self.client.post(
            '/api/v2/parties', json=party_holder, headers={
                "Authorization": "Bearer {}".format(auth_token)}
        )
        json_data = response.get_json()
        self.assertEqual(
            json_data["error"], "User is logged out, Please log in again."
        )
        self.assertEqual(response.status_code, 401)


    def test_zero_length_party_name(self):
        """
        Test api returns correct error code and response message on attempt to
        register a party with no party name
        : return STATUS CODE 400 Bad Request
        """
        # signin admin
        admin_signin = self.admin_signin
        auth_token = self.admin_token

        response = self.client.post(
            '/api/v2/parties',
            json=null_party_name_holder,
            headers={
                "Authorization": "Bearer {}".format(auth_token)
            }
        )
        json_data = response.get_json()
        self.assertIn("Party name does not meet minimum length of 4 letters.",
                      json_data["error"]["party_name"])
        self.assertEqual(response.status_code, 400)

    def test_zero_length_hq_address(self):
        """
        Test api returns correct error code and response message on attempt to
        register a party with no Headquarters details
        : return STATUS CODE 400 Bad Request
        """
        # signin admin
        admin_signin = self.admin_signin
        auth_token = self.admin_token

        response = self.client.post(
            '/api/v2/parties',
            json=null_party_hq_holder,
            headers={
                "Authorization": "Bearer {}".format(auth_token)
            }
        )
        json_data = response.get_json()
        self.assertIn("Please provide party Headquarters address.",
                      json_data["error"]["hq_address"])
        self.assertEqual(response.status_code, 400)

    def test_zero_length_party_fields(self):
        """
        Test api returns correct error code and response message on attempt to
        register a party with no Headquarters details and party name
        : return STATUS CODE 400 Bad Request
        """
        # signin admin
        admin_signin = self.admin_signin
        auth_token = self.admin_token

        response = self.client.post(
            '/api/v2/parties',
            json=null_party_entries_holder,
            headers={
                "Authorization": "Bearer {}".format(auth_token)
            }
        )
        json_data = response.get_json()
        self.assertEqual(json_data["error"]["hq_address"], [
                         "Please provide party Headquarters address."])
        self.assertIn("Party name does not meet minimum length of 4 letters.",
                      json_data["error"]["party_name"])
        self.assertEqual(response.status_code, 400)

    def test_party_name_contain_integer(self):
        """
        Test api returns correct error code and response message on attempt to
        register a party with no party name
        : return STATUS CODE 400 Bad Request
        """
        # signin admin
        admin_signin = self.admin_signin
        auth_token = self.admin_token

        response = self.client.post(
            '/api/v2/parties',
            json=int_party_name_holder,
            headers={
                "Authorization": "Bearer {}".format(auth_token)
            }
        )
        json_data = response.get_json()
        self.assertEqual(json_data["error"], {
                         "party_name": ["Party name cannot contain number(s)."]})
        self.assertEqual(response.status_code, 400)

    def test_register_duplicate_party_name(self):
        """
        Test api returns error message on attempt to register party
        with same party name again.
        :return STATUS CODE 409 Conflict
        """
        response = self.post_data
        self.assertEqual(response.status_code, 201)

        # signin admin
        admin_signin = self.admin_signin
        auth_token = self.admin_token

        response_2 = self.client.post(
            '/api/v2/parties',
            json=party_holder,
            headers={
                "Authorization": "Bearer {}".format(auth_token)
            }
        )
        json_data = response_2.get_json()
        self.assertTrue(
            json_data["error"] == "Try a different Party name, Provided name is taken.")
        self.assertEqual(response_2.status_code, 409)

    def test_get_single_party(self):
        """
        Test api can get a specific party with the provided party id
        from the parties table provided the user is logged in.
        :return: STATUS CODE 200
        """
        # do a post first done by admin user.
        response = self.post_data
        self.assertEqual(response.status_code, 201)

        # signup normal user
        user_signup = self.user_data
        self.assertEqual(user_signup.status_code, 201)

        # signin the user
        user_signin = self.login_data
        json_body = user_signin.get_json()
        auth_token = json_body["data"][0]["token"]
        self.assertTrue(user_signin.status_code, 200)

        # request party with the user logged in token
        get_response = self.client.get(
            'api/v2/parties/1', headers={
                "Authorization": "Bearer {}".format(auth_token)
            }
        )
        self.assertEqual(get_response.status_code, 200)

    def test_party_not_found(self):
        """
        Test api returns correct status code and message when party with an id
        is not found from the database
        :return: STATUS CODE 404
        """
        # signup normal user
        user_signup = self.user_data
        self.assertEqual(user_signup.status_code, 201)

        # signin the user
        user_signin = self.login_data
        json_body = user_signin.get_json()
        auth_token = json_body["data"][0]["token"]
        self.assertTrue(user_signin.status_code, 200)

        get_response = self.client.get(
            'api/v2/parties/3', headers={
                "Authorization": "Bearer {}".format(auth_token)
            }
        )
        self.assertEqual(get_response.status_code, 404)

    def test_get_all_parties(self):
        """
        Test api can all parties from the database when a provided user
        is logged in
        :return: STATUS CODE 200 Ok
        """
        # post a party first
        response = self.post_data
        self.assertEqual(response.status_code, 201)

        # signup normal user
        user_signup = self.user_data
        self.assertEqual(user_signup.status_code, 201)

        # signin the user
        user_signin = self.login_data
        json_body = user_signin.get_json()
        auth_token = json_body["data"][0]["token"]
        self.assertTrue(user_signin.status_code, 200)

        # self.assertEqual(response.status_code, 201)

        get_response = self.client.get(
            'api/v2/parties', headers={
                "Authorization": "Bearer {}".format(auth_token)
            }
        )
        self.assertEqual(get_response.status_code, 200)

    def test_edit_party_name(self):
        """
        Test api can edit a political party, with the a new name and address.
        :return: STATUS CODE 200
        """
        response = self.post_data
        self.assertEqual(response.status_code, 201)
        json_data = response.get_json()
        _id = json_data["data"][0]["party_id"]

        # admin token
        auth_token = self.admin_token

        # edit party details (party name)
        response_edit = self.client.patch(
            'api/v2/parties/{}/name'.format(_id),
            json={
                "party_name": "Changed this"
            },
            headers={
                "Authorization": "Bearer {}".format(auth_token)
            }
        )
        edited_data = self.client.get(
            'api/v2/parties/{}'.format(_id),
            headers={
                "Authorization": "Bearer {}".format(auth_token)
            }
        )
        new_data = edited_data.get_json()
        self.assertEqual(new_data["data"][0]["party_name"], "Changed this")
        self.assertEqual(response_edit.status_code, 200)

    def test_edit_party_error(self):
        """
        Test error returned when the party to edit is not found.
        :return: STATUS CODE 404
        """
        _id = 234  # random id

        # admin token
        auth_token = self.admin_token

        # edit party details (party name)
        response_edit = self.client.patch(
            'api/v2/parties/{}/name'.format(_id),
            json={
                "party_name": "Changed this"
            },
            headers={
                "Authorization": "Bearer {}".format(auth_token)
            }
        )
        new_data = response_edit.get_json()
        self.assertEqual(new_data["error"],
                         "Resource requested for edit not found.")
        self.assertEqual(response_edit.status_code, 404)

    def test_delete_party(self):
        """
        Test api deletes a political party.
        :return: STATUS CODE 200
        """
        response = self.post_data
        self.assertEqual(response.status_code, 201)
        json_data = response.get_json()
        _id = json_data["data"][0]["party_id"]
        response = self.client.delete(
            'api/v1/parties/{}'.format(_id)
        )
        res = response.get_json()
        self.assertEqual(res["data"][0]["message"],
                         "Political Party deleted successfully.")
        self.assertEqual(response.status_code, 200)

    def test_delete_party_error(self):
        """
        Test error message for for non existing party deletion.
        :return: STATUS CODE 404
        """
        _id = uuid.uuid4()
        response = self.client.delete(
            'api/v1/parties/{}'.format(_id)
        )
        res = response.get_json()
        self.assertEqual(res["data"][0]["message"],
                         "Political Party to delete not found.")
        self.assertEqual(response.status_code, 404)
