import requests
import unittest
from unittest.mock import patch

from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
	def create_app(self):
		return app

class TestPrediction(TestBase):
'''
	def test_prediction(self):
		with patch('requests.post') as p:
			p.return_value.text = "Mario Kart,Testing1"
			response = self.client.get(url_for('game_prediction'))
			self.assertIn(b'Blue Shell', response.data)
'''
