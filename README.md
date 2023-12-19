# Count accessible cells for ant

## Условия:
На бесконечной координатной сетке находится муравей. Муравей может перемещаться на 1 клетку вверх (x, y+1),
вниз (x, y-1), влево (x-1, y), вправо (x+1, y) — по одной клетке за шаг. Клетки, в которых сумма цифр в координате X
плюс сумма цифр в координате Y, больше чем 25, недоступны муравью. Например, клетка с координатами (59, 79) недоступна,
т.к. 5+9+7+9=30, что больше 25.

Сколько клеток может посетить муравей, если его начальная позиция (1000, 1000) (включая начальную клетку).

## Решение
Для решения используется алгоритм обхода графа в ширину (BFS)
```python
def test_count_accessible_cells_for_ant_starting_at_1000_1000(self):
        result = count_accessible_cells_for_ant(Point(1000, 1000))
        self.assertEqual(result, 148848)
```
## Простой тест
Начальная точка (1010, 980) -> ответ 28, смотреть тест:
```python
    def test_ant_accessible_cells_count_at_coordinates_1010_980(self):
        result = count_accessible_cells_for_ant(Point(1010, 980))
        self.assertEqual(result, 28)
```
![img.png](static%2Fimg.png)

## Визуализация
Зависит от pyGame
