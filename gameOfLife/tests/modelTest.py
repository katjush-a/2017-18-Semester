import unittest
from model import *


class TestModel(unittest.TestCase):
    def test_origin(self):
        self.assertEqual(currentGen.__scan__(0, 0), 0)

    def test_alive(self):
        self.assertEqual(currentGen.__scan__(0, 2), 1)

    def test_alive_right(self):
        self.assertEqual(currentGen.__scan__(0, 1), 1)

    def test_alive_left(self):
        self.assertEqual(currentGen.__scan__(0, 3), 1)


if __name__ == '__main__':
    unittest.main()
