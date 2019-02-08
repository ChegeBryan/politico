"""Tests for the office api endpoints"""

import uuid

from .base_test import BaseTestData


class OfficeAPITestCase(BaseTestData):
    """
    Class for testing office endpoints
    """

    def test_create_office(self):
        """
        Test api return correct status code on success
        : return STATUS CODE 201 Created
        """

        #  app testing client
        response = self.office_data
        json_body = response.get_json()
        self.assertIsInstance(json_body["data"], list)
        self.assertEqual(response.status_code, 201)

    def test_get_single_office(self):
        """
        Test api can get a specific office with the provided office id
        from the OFFICES list.
        :return: STATUS CODE 200
        """
        # do a post first
        response = self.office_data
        self.assertEqual(response.status_code, 201)
        json_data = response.get_json()
        _id = json_data["data"][0]["officeId"]
        get_response = self.client.get(
            'api/v1/offices/{}'.format(_id)
        )
        self.assertEqual(get_response.status_code, 200)

    def test_office_not_found(self):
        """
        Test api returns correct status code and message when party with an id
        is not found from the PARTIES list.
        :return: STATUS CODE 404
        """
        # do a post first
        response = self.office_data
        self.assertEqual(response.status_code, 201)
        _id = uuid.uuid4()
        get_response = self.client.get(
            'api/v1/offices/{}'.format(_id)
        )
        self.assertEqual(get_response.status_code, 404)

    def test_get_all_offices(self):
        """
        Test api can all offices from the OFFICES list.
        :return: STATUS CODE 200
        """
        # do a post first
        response = self.office_data
        self.assertEqual(response.status_code, 201)
        # add another entry
        response = self.office_data
        self.assertEqual(response.status_code, 201)
        get_response = self.client.get(
            'api/v1/offices'
        )
        self.assertEqual(get_response.status_code, 200)

    def test_office_entered_is_valid(self):
        """
        Test validates if an office name entered is a valid office
        : STATUS CODE 400
        """
        response = self.client.post(
            '/api/v1/offices', json=self.invalid_office_name_holder
        )
        json_body = response.get_json()
        self.assertEqual(json_body["error"]["officeName"][0],
                         "sene not a valid office name. Try one of these president, governor, senator, house of representatives.")
        self.assertEqual(response.status_code, 400)

    def test_office_type_is_valid(self):
        """
        Test to check office type entered is a valid office
        STATUS CODE 400
        """
        response = self.client.post(
            '/api/v1/offices', json=self.invalid_office_type_holder
        )
        json_body = response.get_json()
        self.assertEqual(json_body["error"]["officeType"][0],
                         "cong not a valid office type. Try one of these federal, congress, state.")
        self.assertEqual(response.status_code, 400)
