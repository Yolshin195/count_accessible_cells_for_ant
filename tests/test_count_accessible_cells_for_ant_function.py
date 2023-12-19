import unittest

from app.count_accessible_cells_for_ant import count_accessible_cells_for_ant, Point


class TestCountAccessibleCellsForAnt(unittest.TestCase):
    def test_count_accessible_cells_for_ant_starting_at_1000_1000(self):
        result = count_accessible_cells_for_ant(Point(1000, 1000))
        self.assertEqual(result, 148848)

    def test_ant_accessible_cells_count_at_coordinates_1010_980(self):
        result = count_accessible_cells_for_ant(Point(1010, 980))
        self.assertEqual(result, 28)

    def test_no_accessible_path_from_specific_point(self):
        """
        Тест, чтобы убедиться, что из определенной точки нет доступного пути
        """
        result = count_accessible_cells_for_ant(Point(1004, 995))
        self.assertEqual(result, 0)

        result = count_accessible_cells_for_ant(Point(1005, 988))
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
