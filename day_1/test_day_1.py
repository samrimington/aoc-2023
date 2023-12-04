import unittest

from . import get_calibration_value as f, get_real_calibration_value as g

class TestGetCalibrationValue(unittest.TestCase):
    def test_two_digits(self):
        self.assertEqual(f("1abc2"), 12)
        self.assertEqual(f("pqr3stu8vwx"), 38)

    def test_five_digits(self):
        self.assertEqual(f("a1b2c3d4e5f"), 15)

    def test_one_digit(self):
        self.assertEqual(f("treb7uchet"), 77)

class TestGetRealCalibrationValue(unittest.TestCase):
    def test_two_words(self):
        self.assertEqual(g("two1nine"), 29)
        self.assertEqual(g("eightwothree"), 83)
        self.assertEqual(g("abcone2threexyz"), 13)
        self.assertEqual(g("xtwone3four"), 24)

    def test_three_words(self):
        self.assertEqual(g("4nineeightseven2"), 42)

    def test_one_word(self):
        self.assertEqual(g("zoneight234"), 14)
        self.assertEqual(g("7pqrstsixteen"), 76)

    def test_many_words(self):
        self.assertEqual(g("sixsevenfivefourxf4mzhmkztwonepzt"), 61)

    def test_overlapping_words(self):
        self.assertEqual(g("eighthree"), 83)
        self.assertEqual(g("sevenine"), 79)
