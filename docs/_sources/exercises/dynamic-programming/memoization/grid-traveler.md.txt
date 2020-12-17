# Grid Traveler





Say that you are a traveler on a 2D grid. You begin in the top-left corner and your goal is to travel to the bottom-right corner. You may only move right or down.

In how many ways can you travel to the goal on a grid with dimensions `m * n`?

Write the function `grid_traveler(m, n)` to solve this. Use memoization to get the last tests to pass in a respectable about of time

You can learn more from Free Code Camp's [Dynamic Programming](https://www.youtube.com/watch?v=oBt53YbR9Kk) video.

## Starter Code
```python
def grid_traveler(m: int, n: int) -> int:
    pass
```

## Tests
```python
from main import grid_traveler


def test_grid_traveler_base_case():
    assert grid_traveler(0, 0) == 0
    assert grid_traveler(0, 1) == 0
    assert grid_traveler(1, 0) == 0
    assert grid_traveler(1, 1) == 1


def test_grid_traveler():
    assert grid_traveler(2, 2) == 2
    assert grid_traveler(2, 3) == 3
    assert grid_traveler(3, 3) == 6
    assert grid_traveler(3, 8) == 36


def test_grid_traveler_memo():
    assert grid_traveler(10, 15) == 817190
    assert grid_traveler(30, 30) == 30067266499541040
    assert grid_traveler(100, 100) == 22750883079422934966181954039568885395604168260154104734000
```
