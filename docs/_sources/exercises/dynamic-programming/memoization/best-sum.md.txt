# Best Sum





Write a function `best_sum(target_sum, numbers)` that takes in a `target_sum` and a list of `numbers` as arguments.

The function should return a list containing the shortest combination of numbers that add up to exactly the `target_sum`.

If there is a tie for the shortest combination, you may return any one of the shortest.

You can learn more from Free Code Camp's [Dynamic Programming](https://www.youtube.com/watch?v=oBt53YbR9Kk) video.

## Starter Code
```python
from typing import List


def best_sum(target_sum: int, numbers: List[int]) -> List[int]:
    pass
```

## Tests
```python
from main import best_sum


def test_best_sum_base_case():
    assert best_sum(0, [1, 2, 3]) == []
    assert best_sum(-1, [1, 2, 3]) == None


def test_best_sum():
    assert best_sum(7, [5, 3, 4, 7]) == [7]
    assert best_sum(8, [2, 3, 5]) == [3, 5]
    assert best_sum(8, [1, 4, 5]) == [4, 4]


def test_best_sum_memo():
    assert best_sum(100, [1, 2, 5, 25]) == [25, 25, 25, 25]
```
