import requests
import unittest

from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
	def create_app(self):
		return app

class TestGame(TestBase):

	def test_game(self):
		response = self.client.get(url_for('user_name1'))
		self.assertEqual(response.status_code, 200)
