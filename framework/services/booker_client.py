"""
Created on Oct 13, 2019

@author: majdukovic
"""

from framework.services.rest_client import RestClient
from framework.services.url_generator import UrlGenerator


class BookerClient(RestClient):
    """
    Client to deal with Restful-booker API
    """
    def __init__(self):
        super(BookerClient, self).__init__()
        self.url_generator = UrlGenerator()
        self.rest_client = RestClient()

    def get_all_booking_ids(self):
        """
        Get all booking IDs
        @return: (response, dict)
        """
        url = self.url_generator.get_url('GET_BOOKINGS')
        response = self.get(url, hdrs={'Content-Type': 'application/json'})
        return response, response.json()
