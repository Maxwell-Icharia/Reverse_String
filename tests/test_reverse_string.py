import unittest
from main.reverse_string import reverse_string

class Reverse(unittest.TestCase):
	def test_is_string(self):
		self.assertIsInstance(reverse_string('abc'), str)
	def test_is_equal(self):
		self.assertTrue(reverse_string('dearc'), 'craed')


if __name__ == '__main__':
	unittest.main()