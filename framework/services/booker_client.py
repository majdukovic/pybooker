"""
Created on Oct 13, 2019

@author: majdukovic
"""

from framework.services.rest_client import RestClient
from framework.services.url_generator import UrlGenerator
import json


class BookerClient(RestClient):
    """
    Client to deal with Restful-booker API
    """
    def __init__(self):
        super(BookerClient, self).__init__()
        self.url_generator = UrlGenerator()
        self.rest_client = RestClient()

    def create_auth(self):
        """
        Create authorization token
        @return: (response, dict)
        """
        url = self.url_generator.get_url('POST_TOKEN')
        payload = {"username": "admin", "password": "password123"}
        headers = {'Content-Type': 'application/json'}
        response = self.post(url, data=json.dumps(payload), hdrs=headers)
        return response, response.json()

    def get_all_booking_ids(self):
        """
        Get all booking IDs
        @return: (response, dict)
        """
        url = self.url_generator.get_url('GET_BOOKING')
        headers = {'Content-Type': 'application/json'}
        response = self.get(url, hdrs=headers)
        return response, response.json()

    def delete_all_bookings(self):
        """
        Delete all bookings
        @return: (response, dict)
        """
        token = self.create_auth()
        url = self.url_generator.get_url('DELETE_BOOKING')
        headers = dict()
        headers['Content-Type'] = 'application/json'
        headers['Accept'] = 'application/json'
        headers['Cookie'] = f'{token}'
        param = '1'
        response = self.delete(url, params=json.dumps(param), hdrs=headers)
        print(response)
        return response, response.json()

