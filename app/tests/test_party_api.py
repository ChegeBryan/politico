""" Tests for party api endpoints """
import uuid

from .base_test import BaseTestData
from app.api.db.party_test_data import (
    null_party_entries_holder, null_party_hq_holder, int_party_name_holder, null_party_name_holder, party_holder)


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

    def test_zero_length_party_name(self):
        """
        Test api returns correct error code and response message on attempt to
        register a party with no party name
        : return STATUS CODE 400 Bad Request
        """
        response = self.client.post(
            '/api/v1/parties',
            json=null_party_name_holder
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
        response = self.client.post(
            '/api/v1/parties',
            json=null_party_hq_holder
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
        response = self.client.post(
            '/api/v1/parties',
            json=null_party_entries_holder
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
        response = self.client.post(
            '/api/v1/parties',
            json=int_party_name_holder
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
        response_2 = self.client.post(
            'api/v1/parties', json=party_holder
        )
        json_data = response_2.get_json()
        self.assertTrue(
            json_data["error"] == "Try a different Party name, Provided name is taken.")
        self.assertEqual(response_2.status_code, 409)

    def test_get_single_party(self):
        """
        Test api can get a specific party with the provided party id
        from the PARTIES list.
        :return: STATUS CODE 200
        """
        # do a post first
        response = self.post_data
        self.assertEqual(response.status_code, 201)
        json_data = response.get_json()
        _id = json_data["data"][0]["party_id"]
        get_response = self.client.get(
            'api/v1/parties/{}'.format(_id)
        )
        self.assertEqual(get_response.status_code, 200)

    def test_party_not_found(self):
        """
        Test api returns correct status code and message when party with an id
        is not found from the PARTIES list.
        :return: STATUS CODE 404
        """
        # do a post first
        response = self.post_data
        self.assertEqual(response.status_code, 201)
        _id = uuid.uuid4()
        get_response = self.client.get(
            'api/v1/parties/{}'.format(_id)
        )
        self.assertEqual(get_response.status_code, 404)

    def test_get_all_parties(self):
        """
        Test api can all parties from the PARTIES list.
        :return: STATUS CODE 200
        """
        # do a post first
        response = self.post_data
        self.assertEqual(response.status_code, 201)
        # add another entry
        response = self.client.post(
            '/api/v1/parties',
            json={
                "party_name": "second party",
                "hq_address": "somewhere"
            }
        )
        self.assertEqual(response.status_code, 201)
        get_response = self.client.get(
            'api/v1/parties'
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
        # edit party details (party name)
        response_edit = self.client.patch(
            'api/v1/parties/{}/name'.format(_id),
            json={
                "party_name": "Changed this"
            }
        )
        edited_data = self.client.get(
            'api/v1/parties/{}'.format(_id)
        )
        new_data = edited_data.get_json()
        self.assertEqual(new_data["data"][0]["party_name"], "Changed this")
        self.assertEqual(response_edit.status_code, 200)

    def test_edit_party_error(self):
        """
        Test error returned when the party to edit is not found.
        :return: STATUS CODE 404
        """
        _id = uuid.uuid4()  # generate random id
        # edit party details (party name)
        response_edit = self.client.patch(
            'api/v1/parties/{}/name'.format(_id),
            json={
                "party_name": "Changed this"
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
