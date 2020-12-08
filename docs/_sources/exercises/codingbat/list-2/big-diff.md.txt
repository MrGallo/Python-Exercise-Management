# big_diff





Given an list length 1 or more of ints, return the difference between the largest and smallest values in the list. Note: the built-in Math.min(v1, v2) and Math.max(v1, v2) methods  return the smaller or larger of two values.

```
big_diff([10, 3, 5, 6]) -> 7
big_diff([7, 2, 10, 9]) -> 8
big_diff([2, 10, 7, 2]) -> 8
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p196640) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def big_diff(nums: List[int]) -> int:
    pass


result = big_diff([10, 3, 5, 6])
print(result)
```

## Tests
```python
from main import big_diff


def test_big_diff_1():
    assert big_diff([10, 3, 5, 6]) == 7


def test_big_diff_2():
    assert big_diff([7, 2, 10, 9]) == 8


def test_big_diff_3():
    assert big_diff([2, 10, 7, 2]) == 8


def test_big_diff_4():
    assert big_diff([2, 10]) == 8


def test_big_diff_5():
    assert big_diff([10, 2]) == 8


def test_big_diff_6():
    assert big_diff([10, 0]) == 10


def test_big_diff_7():
    assert big_diff([2, 3]) == 1


def test_big_diff_8():
    assert big_diff([2, 2]) == 0


def test_big_diff_9():
    assert big_diff([2]) == 0


def test_big_diff_10():
    assert big_diff([5, 1, 6, 1, 9, 9]) == 8


def test_big_diff_11():
    assert big_diff([7, 6, 8, 5]) == 3


def test_big_diff_12():
    assert big_diff([7, 7, 6, 8, 5, 5, 6]) == 3
```
