import unittest
from flask_testing import TestCase
from flask import abort, url_for
from application import frontend

class TestBase(TestCase):

    def create_app(self):
        config_name = 'frontend_testing'
        return frontend

class test_frontend(TestBase):

        def test_homepage(self):
            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)
