from http import HTTPStatus as http

import requests


class TestGetBooking:

    def test_get_all_bookings(self):
        url = 'https://restful-booker.herokuapp.com/booking'
        response = requests.get(url=url)

        ''' Verify request was successful '''
        assert response.status_code, http.OK
        print(f'\nStatus code: {response.status_code}')
        print(f'\nJSON: {response.json()}')

