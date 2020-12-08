# sum_67





Return the sum of the numbers in the list, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.

```
sum_67([1, 2, 2]) -> 5
sum_67([1, 2, 2, 6, 99, 99, 7]) -> 5
sum_67([1, 1, 6, 7, 2]) -> 4
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p111327) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def sum_67(nums: List[int]) -> int:
    pass


result = sum_67([1, 2, 2])
print(result)
```

## Tests
```python
from main import sum_67


def test_sum_67_1():
    assert sum_67([1, 2, 2]) == 5


def test_sum_67_2():
    assert sum_67([1, 2, 2, 6, 99, 99, 7]) == 5


def test_sum_67_3():
    assert sum_67([1, 1, 6, 7, 2]) == 4


def test_sum_67_4():
    assert sum_67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7]) == 2


def test_sum_67_5():
    assert sum_67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7]) == 2


def test_sum_67_6():
    assert sum_67([2, 7, 6, 2, 6, 7, 2, 7]) == 18


def test_sum_67_7():
    assert sum_67([2, 7, 6, 2, 6, 2, 7]) == 9


def test_sum_67_8():
    assert sum_67([1, 6, 7, 7]) == 8


def test_sum_67_9():
    assert sum_67([6, 7, 1, 6, 7, 7]) == 8


def test_sum_67_10():
    assert sum_67([6, 8, 1, 6, 7]) == 0


def test_sum_67_11():
    assert sum_67([]) == 0


def test_sum_67_12():
    assert sum_67([6, 7, 11]) == 11


def test_sum_67_13():
    assert sum_67([11, 6, 7, 11]) == 22


def test_sum_67_14():
    assert sum_67([2, 2, 6, 7, 7]) == 11
```
