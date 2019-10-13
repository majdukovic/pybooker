"""
Created on Oct 13, 2019

@author: majdukovic
"""

import requests


class RestClient:
    """
    Class for dealing with generic POSTS/UPDATES/GETS/DELETES
    """
    default_timeout = 10

    def post(self, url=None, data=None, params=None, hdrs=None, ck=None, basic_auth=None, timeout=None):
        response = requests.post(url, data=data, params=params, headers=hdrs, cookies=ck, auth=basic_auth,
                                 timeout=timeout or self.default_timeout)

        return response

    def put(self, url=None, data=None, params=None, hdrs=None, ck=None, basic_auth=None, timeout=None):
        response = requests.put(url, data=data, params=params, headers=hdrs, cookies=ck, auth=basic_auth,
                                timeout=timeout or self.default_timeout)

        return response

    def get(self, url=None, params=None, hdrs=None, ck=None, basic_auth=None, timeout=None):
        response = requests.get(url, params=params, headers=hdrs, cookies=ck, auth=basic_auth,
                                timeout=timeout or self.default_timeout)

        return response

    def delete(self, url, params=None, hdrs=None, ck=None, basic_auth=None, timeout=None):
        response = requests.delete(url, params=params, headers=hdrs, cookies=ck, auth=basic_auth,
                                   timeout=timeout or self.default_timeout)

        return response

    def update(self, url, data=None, params=None, hdrs=None, ck=None, basic_auth=None, timeout=None):
        response = requests.put(url, data=data, params=params, headers=hdrs, cookies=ck, auth=basic_auth,
                                timeout=timeout or self.default_timeout)

        return response

