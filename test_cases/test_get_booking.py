"""
Created on Oct 13, 2019

@author: majdukovic
"""
from http import HTTPStatus as http
from framework.services.booker_client import BookerClient

booker_client = BookerClient()


class TestGetBooking:

    def test_get_all_booking_ids(self):
        """
        This test case verifies user can get all booking IDs
        """
        response, booking_ids = booker_client.get_all_booking_ids()
        assert response.status_code == http.OK, f'Actual status code received: {response.status_code}'
