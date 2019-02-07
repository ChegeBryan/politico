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
