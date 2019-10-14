"""
Created on Oct 13, 2019

@author: majdukovic
"""


class UrlGenerator:
    """
    This class builds urls
    """

    def __init__(self):
        self.urls_map = {
            'POST_TOKEN': 'auth',
            'GET_BOOKING': 'booking',
            'POST_BOOKING': 'booking',
            'PUT_BOOKING': 'booking',
            'PATCH_BOOKING': 'booking',
            'DELETE_BOOKING': 'booking'
        }

    def get_url(self, api_key):
        """
        Return the url registered for the api_key informed.
        @param api_key: The key used to register the url in the url_generator.py
        """
        # Check the api alias is valid or registered already
        if api_key not in self.urls_map:
            raise Exception(f'API alias {api_key} is not registered in known endpoints.')

        # endpoint = f'https://restful-booker.herokuapp.com/{self.urls_map[api_key]}'
        endpoint = f'http://localhost:3001/{self.urls_map[api_key]}'
        return endpoint
