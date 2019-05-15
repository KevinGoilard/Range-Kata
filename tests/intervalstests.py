import unittest
from intervals.intervals import Interval
from intervals.intervals import StartLimit
from intervals.intervals import EndLimit


class IntervalsTests(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_interval_contains_return_true(self):
        interval = Interval(StartLimit(2), EndLimit(6))

        result = interval.contains({2, 4})

        self.assertTrue(result)

    def test_interval_contains_return_false(self):
        interval = Interval(StartLimit(2), EndLimit(6))

        result = interval.contains({-1, 3})

        self.assertFalse(result)

    def test_interval_contains_return_false_triangulation(self):
        interval = Interval(StartLimit(2), EndLimit(6))

        result = interval.contains({3, 7})

        self.assertFalse(result)

    def test_interval_with_open_limit_contains_his_endpoint(self):
        interval = Interval(StartLimit(2), EndLimit(6))

        result = interval.contains({6})

        self.assertTrue(result)

    def test_interval_with_close_limit_not_contains_his_endpoint(self):
        interval = Interval(StartLimit(2), EndLimit(6, False))

        result = interval.contains({6})

        self.assertFalse(result)

    def test_interval_with_open_limit_contains_his_startpoint(self):
        interval = Interval(StartLimit(2), EndLimit(6))

        result = interval.contains({2})

        self.assertTrue(result)

    def test_interval_with_close_limit_not_contains_his_startpoint(self):
        interval = Interval(StartLimit(2, False), EndLimit(6))

        result = interval.contains({2})

        self.assertFalse(result)

    def test_interval_can_return_all_his_points(self):
        interval = Interval(StartLimit(2), EndLimit(6))

        result = interval.get_all_points()

        self.assertEqual({2, 3, 4, 5, 6}, result)

    def test_interval_can_return_all_his_points_end_closed(self):
        interval = Interval(StartLimit(2), EndLimit(4, False))

        result = interval.get_all_points()

        self.assertEqual({2, 3}, result)

    def test_interval_can_return_all_his_points_start_closed(self):
        interval = Interval(StartLimit(2, False), EndLimit(4))

        result = interval.get_all_points()

        self.assertEqual({3, 4}, result)

    def test_interval_can_return_all_his_points_start_closed(self):
        interval = Interval(StartLimit(2, False), EndLimit(4,False))

        result = interval.get_all_points()

        self.assertEqual({3}, result)
