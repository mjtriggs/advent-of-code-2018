# Unit Tests for Day 1

import unittest
from day1 import GetResultingFrequency
from day1 import FreqReachedTwice

class TestGetResultingFrequency(unittest.TestCase):
    def test_output(self):
        # Test that this works for correct values
        self.assertEqual(GetResultingFrequency(0, [+1, -1]), 0)
        self.assertEqual(GetResultingFrequency(1, [+1, -1]), 1)
        self.assertEqual(GetResultingFrequency(2, [+2, -1]), 3)
        # And now things that should fall over
        self.assertRaises(TypeError, GetResultingFrequency, 0, 1)
        self.assertRaises(TypeError, GetResultingFrequency, 0, True)
        # I hope my tests can get better with time

class TestFreqReachedTwice(unittest.TestCase):
    def test_output(self):
        self.assertEqual(FreqReachedTwice(0, [1, 1, -1]), 1)
        self.assertEqual(FreqReachedTwice(0, [1, -1]), 0)
        self.assertEqual(FreqReachedTwice(0, [3, 3, 4, -2, -4]), 10)
        self.assertEqual(FreqReachedTwice(0, [-6, 3, 8, 5, -6]), 5)
        self.assertEqual(FreqReachedTwice(0, [7, 7, -2, -7, -4]), 14)
