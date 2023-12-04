import unittest

from . import Card

class TestCardClass(unittest.TestCase):
    def test_winning_card(self):
        a = Card("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53")
        self.assertEqual(a.winning, [41, 48, 83, 86, 17])
        self.assertEqual(a.scoring, [83, 86, 6, 31, 17, 9, 48, 53])
        self.assertEqual(a.points(), 8)

    def test_losing_card(self):
        a = Card("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36")
        self.assertEqual(a.winning, [87, 83, 26, 28, 32])
        self.assertEqual(a.scoring, [88, 30, 70, 12, 93, 22, 82, 36])
        self.assertEqual(a.points(), 0)
