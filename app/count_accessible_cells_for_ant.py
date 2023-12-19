"""
На бесконечной координатной сетке находится муравей. Муравей может перемещаться на 1 клетку вверх (x, y+1),
вниз (x, y-1), влево (x-1, y), вправо (x+1, y), по одной клетке за шаг. Клетки, в которых сумма цифр в координате X
плюс сумма цифр в координате Y больше чем 25, недоступны муравью. Например, клетка с координатами (59, 79) недоступна,
т.к. 5+9+7+9=30, что больше 25. Сколько клеток может посетить муравей, если его начальная позиция (1000, 1000)
(включая начальную клетку).
"""
from dataclasses import dataclass
from collections import deque


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


direction = [Point(0, 1), Point(0, -1), Point(-1, 0), Point(1, 0)]


def sum_of_digits(num):
    """
    Вычисляет сумму цифр в заданном числе.

    :param num: Целое число.
    :return: Сумма цифр в числе.
    :raise ValueError: Если число отрицательное
    """
    try:
        return sum(int(digit) for digit in str(num))
    except ValueError:
        raise ValueError("Number cannot be negative.")


def is_accessible(point: Point):
    """
    Проверяет, является ли клетка доступной для муравья.

    :param point: Объект Point, представляющий координаты клетки.
    :return: True, если клетка доступна, иначе False.
    """
    return (
        point.x >= 0
        and point.y >= 0
        and sum_of_digits(point.x) + sum_of_digits(point.y) <= 25
    )


def count_accessible_cells_for_ant(start_point: Point) -> int:
    """
    Определяет количество клеток, которые муравей может посетить, начиная с заданной начальной позиции.

    :param start_point: Начальная позиция муравья, представленная объектом Point.
    :return: Количество посещенных клеток.
    """
    visited = set()
    queue = deque([start_point])

    accessible_cells = 0

    while queue:
        current_position = queue.popleft()

        if current_position not in visited and is_accessible(current_position):
            visited.add(current_position)
            accessible_cells += 1
            queue.extend([current_position + move for move in direction])

    return accessible_cells


if __name__ == "__main__":
    print(count_accessible_cells_for_ant(Point(1000, 1000)))
