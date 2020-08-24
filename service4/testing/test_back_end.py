import requests
import unittest
from unittest.mock import patch

from flask import url_for, request
from flask_testing import TestCase

from application import app, routes


class TestBase(TestCase):
	def create_app(self):
		return app

class TestService4(TestBase):

	def test_prediction(self):
		response = self.client.get(url_for('game_prediction'))
		self.assertEqual(response.status_code, 500)
	

