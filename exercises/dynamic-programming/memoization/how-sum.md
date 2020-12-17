# How Sum





Write a function `how_sum(target_sum, numbers)` that takes in a `target_sum` and a list of `numbers` as arguments.

The function should return a list containing any combination of elements that add up to exactly the `target_sum`. If there is no combination that adds up to the `target_sum` then return `None`.

If there are multiple combinations possible, you may return any single one.

You can learn more from Free Code Camp's [Dynamic Programming](https://www.youtube.com/watch?v=oBt53YbR9Kk) video.

## Starter Code
```python
from typing import List


def how_sum(target_sum: int, numbers: List[int]) -> List[int]:
    pass
```

## Tests
```python
from main import how_sum


def test_how_sum_base_case():
    assert how_sum(0, [1, 2, 3]) == []
    assert how_sum(-1, [1, 2, 3]) == None
    assert how_sum(1, [2, 3]) == None


def test_how_sum():
    assert how_sum(1, [1, 2, 3]) == [1]
    assert sum(how_sum(7, [2, 3])) == 7
    assert sum(how_sum(7, [5, 3, 4, 7])) == 7
    assert sum(how_sum(8, [2, 3, 5])) == 8
    assert how_sum(7, [2, 4]) == None


def test_how_sum_memo():
    assert how_sum(300, [7, 14]) == None
```
