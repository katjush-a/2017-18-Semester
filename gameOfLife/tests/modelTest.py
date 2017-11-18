import unittest
from model import *

testGrid = [[0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 1, 1]]


class TestModel(unittest.TestCase):
    def test_dead(self):
        self.assertEqual(scan(testGrid, 0, 0), 0)

if __name__ == '__main__':
    unittest.main()
