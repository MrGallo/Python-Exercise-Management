# centered_average





Return the "centered" average of an list of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the list. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the list is length 3 or more.

```
centered_average([1, 2, 3, 4, 100]) -> 3
centered_average([1, 1, 5, 5, 10, 8, 7]) -> 5
centered_average([-10, -4, -2, -4, -2, 0]) -> -3
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p136585) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def centered_average(nums: List[int]) -> int:
    pass


result = centered_average([1, 2, 3, 4, 100])
print(result)
```

## Tests
```python
from main import centered_average


def test_centered_average_1():
    assert centered_average([1, 2, 3, 4, 100]) == 3


def test_centered_average_2():
    assert centered_average([1, 1, 5, 5, 10, 8, 7]) == 5


def test_centered_average_3():
    assert centered_average([-10, -4, -2, -4, -2, 0]) == -3


def test_centered_average_4():
    assert centered_average([5, 3, 4, 6, 2]) == 4


def test_centered_average_5():
    assert centered_average([5, 3, 4, 0, 100]) == 4


def test_centered_average_6():
    assert centered_average([100, 0, 5, 3, 4]) == 4


def test_centered_average_7():
    assert centered_average([4, 0, 100]) == 4


def test_centered_average_8():
    assert centered_average([0, 2, 3, 4, 100]) == 3


def test_centered_average_9():
    assert centered_average([1, 1, 100]) == 1


def test_centered_average_10():
    assert centered_average([7, 7, 7]) == 7


def test_centered_average_11():
    assert centered_average([1, 7, 8]) == 7


def test_centered_average_12():
    assert centered_average([1, 1, 99, 99]) == 50


def test_centered_average_13():
    assert centered_average([1000, 0, 1, 99]) == 50


def test_centered_average_14():
    assert centered_average([4, 4, 4, 4, 5]) == 4


def test_centered_average_15():
    assert centered_average([4, 4, 4, 1, 5]) == 4


def test_centered_average_16():
    assert centered_average([6, 4, 8, 12, 3]) == 6
```
