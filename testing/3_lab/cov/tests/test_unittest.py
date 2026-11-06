import unittest

from cov.score import calculate_average, describe_result


class TestScoreWithUnittest(unittest.TestCase):
    def test_calculate_average(self):
        self.assertEqual(calculate_average([70, 80, 90]), 80)

    def test_calculate_average_for_empty_list(self):
        self.assertEqual(calculate_average([]), 0.0)

    def test_describe_result_for_each_result(self):
        self.assertEqual(describe_result(95), "excellent")
        self.assertEqual(describe_result(60), "passed")
        self.assertEqual(describe_result(40), "failed")

    def test_describe_result_rejects_score_outside_range(self):
        with self.assertRaises(ValueError):
            describe_result(101)


if __name__ == "__main__":
    unittest.main()
