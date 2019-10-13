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
            'GET_BOOKINGS': 'booking',
        }

    def get_url(self, api_key):
        """
        Return the url registered for the api_key informed.
        @param api_key: The key used to register the url in the url_generator.py
        """
        # Check the api alias is valid or registered already
        if api_key not in self.urls_map:
            raise Exception(f'API alias {api_key} is not registered in known endpoints.')

        endpoint = f'https://restful-booker.herokuapp.com/{self.urls_map[api_key]}'
        return endpoint
