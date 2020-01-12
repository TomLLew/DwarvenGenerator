import unittest
from flask_testing import TestCase
from flask import abort, url_for
from service1.application import service1

class TestBase(TestCase):

    def create_app(self):
        config_name = 'service1_testing'
        return service1


class test_service1(TestBase):

    def test_homepage(self):
        response = self.client.get(url_for('name'))
        self.assertEqual(response.status_code, 200)