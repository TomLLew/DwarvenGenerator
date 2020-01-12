import unittest
from flask_testing import TestCase
from flask import abort, url_for
from service1.application import service3

class TestBase(TestCase):

    def create_app(self):
        config_name = 'service3_testing'
        return service3


class test_service3(TestBase):

    def test_homepage(self):
        response = self.client.get(url_for('stats'))
        self.assertEqual(response.status_code, 200)