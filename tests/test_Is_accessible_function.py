import unittest

from app.count_accessible_cells_for_ant import Point, is_accessible


class TestIsAccessibleFunction(unittest.TestCase):
    def test_accessible_point(self):
        """
        Тест, когда точка является доступной
        """
        accessible_point = Point(3, 4)
        self.assertTrue(is_accessible(accessible_point))

    def test_not_accessible_negative_coordinates(self):
        """
        Тест, когда точка имеет отрицательные координаты
        """
        not_accessible_point = Point(-1, 5)
        self.assertFalse(is_accessible(not_accessible_point))

    def test_not_accessible_sum_of_digits_exceeds_limit(self):
        """
        Тест, когда сумма цифр координат превышает 25
        Сумма цифр: 1 + 9 + 9 + 8 = 27
        """
        not_accessible_point = Point(199, 8)
        self.assertFalse(is_accessible(not_accessible_point))

    def test_accessible_maximum_values(self):
        """
        Тест, когда точка на грани допустимых значений
        Сумма цифр: 9 + 6 + 9 + 1 = 25
        """
        accessible_point = Point(96, 91)
        self.assertTrue(is_accessible(accessible_point))

    def test_accessible_zero_values(self):
        """
        Тест, когда точка имеет значения 0
        """
        accessible_point = Point(0, 0)
        self.assertTrue(is_accessible(accessible_point))


if __name__ == "__main__":
    unittest.main()
