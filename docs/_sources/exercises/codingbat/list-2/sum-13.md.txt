# sum_13





Return the sum of the numbers in the list, returning 0 for an empty list. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

```
sum_13([1, 2, 2, 1]) -> 6
sum_13([1, 1]) -> 2
sum_13([1, 2, 2, 1, 13]) -> 6
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p127384) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def sum_13(nums: List[int]) -> int:
    pass


result = sum_13([1, 2, 2, 1])
print(result)
```

## Tests
```python
from main import sum_13


def test_sum_13_1():
    assert sum_13([1, 2, 2, 1]) == 6


def test_sum_13_2():
    assert sum_13([1, 1]) == 2


def test_sum_13_3():
    assert sum_13([1, 2, 2, 1, 13]) == 6


def test_sum_13_4():
    assert sum_13([1, 2, 13, 2, 1, 13]) == 4


def test_sum_13_5():
    assert sum_13([13, 1, 2, 13, 2, 1, 13]) == 3


def test_sum_13_6():
    assert sum_13([]) == 0


def test_sum_13_7():
    assert sum_13([13]) == 0


def test_sum_13_8():
    assert sum_13([13, 13]) == 0


def test_sum_13_9():
    assert sum_13([13, 0, 13]) == 0


def test_sum_13_10():
    assert sum_13([13, 1, 13]) == 0


def test_sum_13_11():
    assert sum_13([5, 7, 2]) == 14


def test_sum_13_12():
    assert sum_13([5, 13, 2]) == 5


def test_sum_13_13():
    assert sum_13([0]) == 0


def test_sum_13_14():
    assert sum_13([13, 0]) == 0
```
