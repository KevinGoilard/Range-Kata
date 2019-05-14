import unittest
from intervals.intervals import Interval


class IntervalsTests(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_interval_contains_return_true(self):
        interval = Interval(2, 6)

        result = interval.contains({2, 4})

        self.assertTrue(result)

    def test_interval_contains_return_false(self):
        interval = Interval(2, 6)

        result = interval.contains({-1, 1, 6, 10})

        self.assertFalse(result)

    def test_interval_contains_return_false_triangulation(self):
        interval = Interval(2, 6)

        result = interval.contains({3, 7})

        self.assertFalse(result)
