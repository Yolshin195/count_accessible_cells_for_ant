import unittest

from app.count_accessible_cells_for_ant import sum_of_digits


class TestSumOfDigitsFunction(unittest.TestCase):
    def test_single_digit_number(self):
        self.assertEqual(sum_of_digits(5), 5)

    def test_multiple_digit_number(self):
        self.assertEqual(sum_of_digits(123), 6)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            sum_of_digits(-456)

    def test_zero(self):
        self.assertEqual(sum_of_digits(0), 0)

    def test_large_number(self):
        self.assertEqual(sum_of_digits(9876543210), 45)

    def test_string_input(self):
        with self.assertRaises(ValueError):
            sum_of_digits("abc")


if __name__ == "__main__":
    unittest.main()
