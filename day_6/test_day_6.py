import unittest

from . import get_winning_races as f

class TestGetWinningRaces(unittest.TestCase):
    def test_races(self):
        self.assertEqual(f(7, 9), [2, 3, 4, 5])
        self.assertEqual(f(15, 40), list(range(4, 12)))
        self.assertEqual(f(30, 200), list(range(11, 20)))
        self.assertEqual(f(71530, 940200), list(range(14, 71517)))
