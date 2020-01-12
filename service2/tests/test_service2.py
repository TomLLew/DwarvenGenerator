import unittest, pytest, mock, module
from flask_testing import TestCase
from flask import abort, url_for
from application import service2

class TestBase(TestCase):

    def create_app(self):
        config_name = 'service2_testing'
        return service2

    def setUp(self):
        pass

    def tearDown(self):
        pass

class mulitpletests(TestBase):

    def test_homepage(self):
        response = self.client.get(url_for('job'))
        self.assertEqual(response.status_code, 200)

    def test_random():
        with mock.patch.object(__builtins__, 'input', lambda: {"gender":"Male"}):
            assert module.function() == {"clan":"*", "job":"*"}