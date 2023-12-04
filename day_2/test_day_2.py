import unittest

from . import Game, GameSet

class TestGameClass(unittest.TestCase):
    def test_possible_game(self):
        a = Game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
        self.assertEqual(a.index, 1)
        self.assertEqual(len(a.sets), 3)
        self.assertEqual(a.sets[0], GameSet(4, 0, 3))
        self.assertEqual(a.sets[1], GameSet(1, 2, 6))
        self.assertEqual(a.sets[2], GameSet(0, 2, 0))
        self.assertTrue(a.possible(GameSet(12, 13, 14)))
        self.assertEqual(a.minimum(), GameSet(4, 2, 6))

    def test_impossible_game(self):
        a = Game("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red")
        self.assertEqual(a.index, 3)
        self.assertEqual(len(a.sets), 3)
        self.assertEqual(a.sets[0], GameSet(20, 8, 6))
        self.assertEqual(a.sets[1], GameSet(4, 13, 5))
        self.assertEqual(a.sets[2], GameSet(1, 5, 0))
        self.assertFalse(a.possible(GameSet(12, 13, 14)))
        self.assertEqual(a.minimum(), GameSet(20, 13, 6))

    def test_game_set(self):
        self.assertGreaterEqual(GameSet(1, 1, 1), GameSet(1, 1, 1))
        self.assertGreaterEqual(GameSet(1, 1, 1), GameSet(1, 1, 0))
        self.assertGreaterEqual(GameSet(1, 1, 1), GameSet(0, 1, 0))
        self.assertLessEqual(GameSet(1, 0, 0), GameSet(0, 1, 0))
