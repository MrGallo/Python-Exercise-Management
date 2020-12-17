# Can Sum





Write a function `can_sum(target_sum, numbers)` that takes in a `target_sum` and a list of numbers as arguments.

The function should return a boolean indicating whether or not it is possible to genreate the `target_sum` using numbers from the list.

You may use an element of the list as many times as needed. You may assume that all input numbers are nonnegative.

You can learn more from Free Code Camp's [Dynamic Programming](https://www.youtube.com/watch?v=oBt53YbR9Kk) video.

## Starter Code
```python
from typing import List


def can_sum(target_sum: int, numbers: List[int]):
    pass
```

## Tests
```python
from main import can_sum


def test_can_sum_base_case():
    assert can_sum(0, [1, 2, 3]) == True
    assert can_sum(-1, [1, 2, 3]) == False


def test_can_sum():
    assert can_sum(1, [1, 2, 3]) == True
    assert can_sum(5, [1, 2, 3]) == True
    assert can_sum(5, [3, 6, 7]) == False
    assert can_sum(11, [3, 6, 7]) == False
    assert can_sum(8, [2, 3, 5]) == True


def test_can_sum_memo():
    assert can_sum(300, [7, 14]) == False
```
