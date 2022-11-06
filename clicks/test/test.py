from django.test import TestCase
import requests


class ClicksTestCase(TestCase):
    def test_route_first_example(self):
        response = requests.get('http://127.0.0.1:8000/clicks/4510461/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, '13')

    def test_route_second_example(self):
        response = requests.get(
            'http://127.0.0.1:8000/clicks/4510461/?startdate=2021-11-07%2003:10:00&enddate=2021-11-07%2003:30:00')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, '4')

    def test_route_incorrect_format_example(self):
        response = requests.get(
            'http://127.0.0.1:8000/clicks/4510461/?startdate=2021-11/07%2003:10:00&enddate=2021-11-07%2003:30:00')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.text, 'At least one of the dates is in incorrect format. Expected format is '
                                        '"yyyy-mm-dd hh:mm:ss".Try again.')
