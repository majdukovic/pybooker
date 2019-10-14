"""
Created on Oct 13, 2019

@author: majdukovic
"""
from http import HTTPStatus as http
from framework.services.booker_client import BookerClient
import pytest

booker_client = BookerClient()


@pytest.mark.usefixtures("clear_env")
class TestGetBooking:
    # def test_get_all_booking_ids(self):
    #     """
    #     This test case verifies user can get all booking IDs
    #     """
    #     response, booking_ids = booker_client.get_all_booking_ids()
    #     assert response.status_code == http.OK, f'Actual status code received: {response.status_code}'
    #     print(booking_ids)

    def test_create_auth(self):
        booker_client.delete_all_bookings()
