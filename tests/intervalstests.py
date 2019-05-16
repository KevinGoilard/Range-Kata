import unittest
from parameterized import parameterized
from intervals.intervals import Interval
from intervals.intervals import StartLimit
from intervals.intervals import EndLimit


class IntervalsTests(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_interval_contains_return_true(self):
        interval = Interval(StartLimit(2), EndLimit(6))

        result = interval.contains({3, 4})

        self.assertTrue(result)

    def test_interval_contains_return_false(self):
        interval = Interval(StartLimit(2), EndLimit(6))

        result = interval.contains({-1, 3})

        self.assertFalse(result)

    def test_interval_contains_return_false_triangulation(self):
        interval = Interval(StartLimit(2), EndLimit(6))

        result = interval.contains({3, 7})

        self.assertFalse(result)

    def test_interval_with_open_limit_not_contains_his_endpoint(self):
        interval = Interval(StartLimit(2), EndLimit(6))

        result = interval.contains({6})

        self.assertFalse(result)

    def test_interval_with_close_limit_contains_his_endpoint(self):
        interval = Interval(StartLimit(2), EndLimit(6, False))

        result = interval.contains({6})

        self.assertTrue(result)

    def test_interval_with_open_limit_not_contains_his_startpoint(self):
        interval = Interval(StartLimit(2), EndLimit(6))

        result = interval.contains({2})

        self.assertFalse(result)

    def test_interval_with_close_limit_contains_his_startpoint(self):
        interval = Interval(StartLimit(2, False), EndLimit(6))

        result = interval.contains({2})

        self.assertTrue(result)

    def test_interval_can_return_all_his_points(self):
        interval = Interval(StartLimit(2), EndLimit(6))

        result = interval.get_all_points()

        self.assertEqual({3, 4, 5}, result)

    def test_interval_can_return_all_his_points_end_closed(self):
        interval = Interval(StartLimit(2), EndLimit(4, False))

        result = interval.get_all_points()

        self.assertEqual({3, 4}, result)

    def test_interval_can_return_all_his_points_start_closed(self):
        interval = Interval(StartLimit(2, False), EndLimit(4))

        result = interval.get_all_points()

        self.assertEqual({2, 3}, result)

    def test_interval_can_return_all_his_points_start_and_end_closed(self):
        interval = Interval(StartLimit(2, False), EndLimit(4, False))

        result = interval.get_all_points()

        self.assertEqual({2, 3, 4}, result)

    def test_interval_return_end_points_start_and_end_open(self):
        interval = Interval(StartLimit(2), EndLimit(4))

        result = interval.end_points()

        self.assertEqual([3, 3], result)

    def test_interval_return_end_points_start_closed(self):
        interval = Interval(StartLimit(2, False), EndLimit(4))

        result = interval.end_points()

        self.assertEqual([2, 3], result)

    def test_interval_return_end_points_end_closed(self):
        interval = Interval(StartLimit(2), EndLimit(4, False))

        result = interval.end_points()

        self.assertEqual([3, 4], result)

    def test_interval_return_end_points_start_and_end_closed(self):
        interval = Interval(StartLimit(2, False), EndLimit(4, False))

        result = interval.end_points()

        self.assertEqual([2, 4], result)

    @parameterized.expand([
        (Interval(StartLimit(3, False), EndLimit(5)), Interval(StartLimit(3, False), EndLimit(5)), True),
        (Interval(StartLimit(2, False), EndLimit(10)), Interval(StartLimit(3, False), EndLimit(5)), False),
        (Interval(StartLimit(3, False), EndLimit(5)), Interval(StartLimit(3, False), EndLimit(5, False)), False),
        (Interval(StartLimit(3, False), EndLimit(5)), Interval(StartLimit(3), EndLimit(5)), False)
    ])
    def test_interval_equals(self, interval, other_interval, expected):
        result = interval.equals(other_interval)

        self.assertEqual(result, expected)

    @parameterized.expand([
        (Interval(StartLimit(2), EndLimit(5)), Interval(StartLimit(2), EndLimit(5)), True),
        (Interval(StartLimit(2), EndLimit(5)), Interval(StartLimit(2, False), EndLimit(5)), False),
        (Interval(StartLimit(2), EndLimit(5)), Interval(StartLimit(3), EndLimit(10)), False),
        (Interval(StartLimit(2), EndLimit(5)), Interval(StartLimit(0), EndLimit(4)), False),
        (Interval(StartLimit(2), EndLimit(5)), Interval(StartLimit(3), EndLimit(5, False)), False),
        (Interval(StartLimit(2), EndLimit(5)), Interval(StartLimit(3), EndLimit(5)), True),
        (Interval(StartLimit(2, False), EndLimit(5, False)), Interval(StartLimit(3), EndLimit(5)), True),
        (Interval(StartLimit(2, False), EndLimit(5, False)), Interval(StartLimit(1, False), EndLimit(6, False)), False)
    ])
    def test_interval_contains_interval(self, interval, other_interval, expected):
        result = interval.contains_interval(other_interval)

        self.assertEqual(result, expected)
