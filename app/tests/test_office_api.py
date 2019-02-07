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
