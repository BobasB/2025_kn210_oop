import unittest
from lab_main.main import check_passed_parameter, count_passed_parameters


class TestCountPassedParameters(unittest.TestCase):
    def test_count_passed_parameters(self):
        self.assertEqual(
            count_passed_parameters(1, 2, 3),
            3,
            "Очікується, що функція поверне 3, коли передано три параметри",
        )
        self.assertEqual(count_passed_parameters("a", "b"), 2)
        self.assertEqual(count_passed_parameters(), 0)


if __name__ == "__main__":
    unittest.main()