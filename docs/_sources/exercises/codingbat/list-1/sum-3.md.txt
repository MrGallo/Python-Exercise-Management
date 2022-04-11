# sum_3





Given a list of ints length 3, return the sum of all the elements.

```
sum_3([1, 2, 3]) -> 6
sum_3([5, 11, 2]) -> 18
sum_3([7, 0, 0]) -> 7
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p175763) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def sum_3(nums: List[int]) -> int:
    pass


result = sum_3([1, 2, 3])
print(result)
```

## Tests
```python
from main import sum_3


def test_sum_3_1():
    assert sum_3([1, 2, 3]) == 6


def test_sum_3_2():
    assert sum_3([5, 11, 2]) == 18


def test_sum_3_3():
    assert sum_3([7, 0, 0]) == 7


def test_sum_3_4():
    assert sum_3([1, 2, 1]) == 4


def test_sum_3_5():
    assert sum_3([1, 1, 1]) == 3


def test_sum_3_6():
    assert sum_3([2, 7, 2]) == 11
```
