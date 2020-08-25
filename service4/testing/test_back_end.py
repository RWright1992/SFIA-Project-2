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

	def test_response(self):
		response = self.client.post(url_for('game_prediction'), data='Mario Kark,Test1')
		self.assertEqual(response.status_code, 200)

	def test_jive(self):
		response = self.client.post(url_for('game_prediction'), data='Mario Kark,Test1')
		self.assertIn(b'Turkey', response.data)

	def test_mario_0(self):
		response = self.client.post(url_for('game_prediction'), data='Test0,Mario Kart')
		self.assertIn(b'outside', response.data)

	def test_mario_1(self):
		response = self.client.post(url_for('game_prediction'), data='Test1,Mario Kart')
		self.assertIn(b'Shell', response.data)

	def test_mario_2(self):
		response = self.client.post(url_for('game_prediction'), data='Test2,Mario Kart')
		self.assertIn(b'2nd', response.data)

	def test_mario_3(self):
		response = self.client.post(url_for('game_prediction'), data='Test3,Mario Kart')
		self.assertIn(b'3rd', response.data)

	def test_mario_4(self):
		response = self.client.post(url_for('game_prediction'), data='Test4,Mario Kart')
		self.assertIn(b'4th', response.data)

	def test_mario_5(self):
		response = self.client.post(url_for('game_prediction'), data='Test5,Mario Kart')
		self.assertIn(b'5th', response.data)

	def test_mario_6(self):
		response = self.client.post(url_for('game_prediction'), data='Test6,Mario Kart')
		self.assertIn(b'6th', response.data)

	def test_mario_7(self):
		response = self.client.post(url_for('game_prediction'), data='Test7,Mario Kart')
		self.assertIn(b'7th', response.data)

	def test_mario_8(self):
		response = self.client.post(url_for('game_prediction'), data='Test8,Mario Kart')
		self.assertIn(b'8th', response.data)

	def test_mario_9(self):
		response = self.client.post(url_for('game_prediction'), data='Test9,Mario Kart')
		self.assertIn(b'9th', response.data)

	def test_tetris_0(self):
		response = self.client.post(url_for('game_prediction'), data='Test0,Tetris 99')
		self.assertIn(b'knitting', response.data)

	def test_tetris_1(self):
		response = self.client.post(url_for('game_prediction'), data='Test1,Tetris 99')
		self.assertIn(b'Tetris Maximus', response.data)

	def test_tetris_2(self):
		response = self.client.post(url_for('game_prediction'), data='Test2,Tetris 99')
		self.assertIn(b'2nd', response.data)

	def test_tetris_3(self):
		response = self.client.post(url_for('game_prediction'), data='Test3,Tetris 99')
		self.assertIn(b'3rd', response.data)

	def test_tetris_4(self):
		response = self.client.post(url_for('game_prediction'), data='Test4,Tetris 99')
		self.assertIn(b'4th', response.data)

	def test_tetris_5(self):
		response = self.client.post(url_for('game_prediction'), data='Test5,Tetris 99')
		self.assertIn(b'5th', response.data)

	def test_tetris_6(self):
		response = self.client.post(url_for('game_prediction'), data='Test6,Tetris 99')
		self.assertIn(b'6th', response.data)

	def test_tetris_7(self):
		response = self.client.post(url_for('game_prediction'), data='Test7,Tetris 99')
		self.assertIn(b'7th', response.data)

	def test_tetris_8(self):
		response = self.client.post(url_for('game_prediction'), data='Test8,Tetris 99')
		self.assertIn(b'8th', response.data)

	def test_tetris_9(self):
		response = self.client.post(url_for('game_prediction'), data='Test9,Tetris 99')
		self.assertIn(b'9th', response.data)

	def test_monster_0(self):
		response = self.client.post(url_for('game_prediction'), data='Test0,Monster Hunter Generations')
		self.assertIn(b'Danger', response.data)

	def test_monster_1(self):
		response = self.client.post(url_for('game_prediction'), data='Test1,Monster Hunter Generations')
		self.assertIn(b'Are you really sure', response.data)

	def test_monster_2(self):
		response = self.client.post(url_for('game_prediction'), data='Test2,Monster Hunter Generations')
		self.assertIn(b'boyo', response.data)

	def test_monster_3(self):
		response = self.client.post(url_for('game_prediction'), data='Test3,Monster Hunter Generations')
		self.assertIn(b'better hunting gear', response.data)

	def test_monster_4(self):
		response = self.client.post(url_for('game_prediction'), data='Test4,Monster Hunter Generations')
		self.assertIn(b'materials', response.data)

	def test_monster_5(self):
		response = self.client.post(url_for('game_prediction'), data='Test5,Monster Hunter Generations')
		self.assertIn(b'cool', response.data)

	def test_monster_6(self):
		response = self.client.post(url_for('game_prediction'), data='Test6,Monster Hunter Generations')
		self.assertIn(b'Better eat', response.data)

	def test_monster_7(self):
		response = self.client.post(url_for('game_prediction'), data='Test7,Monster Hunter Generations')
		self.assertIn(b'Maybe hunt', response.data)

	def test_monster_8(self):
		response = self.client.post(url_for('game_prediction'), data='Test8,Monster Hunter Generations')
		self.assertIn(b"I wouldn't", response.data)

	def test_monster_9(self):
		response = self.client.post(url_for('game_prediction'), data='Test9,Monster Hunter Generations')
		self.assertIn(b'Save', response.data)
