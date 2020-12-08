# zero_max





Return a version of the given list where each zero value in the list is replaced by the largest odd value to the right of the zero in the list. If there is no odd value to the right of the zero, leave the zero as a zero.

```
zero_max([0, 5, 0, 3]) -> [5, 5, 3, 3]
zero_max([0, 4, 0, 3]) -> [3, 4, 3, 3]
zero_max([0, 1, 0]) -> [1, 1, 0]
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p187050) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def zero_max(nums: List[int]) -> List[int]:
    pass


result = zero_max([0, 5, 0, 3])
print(result)
```

## Tests
```python
from main import zero_max


def test_zero_max_1():
    assert zero_max([0, 5, 0, 3]) == [5, 5, 3, 3]


def test_zero_max_2():
    assert zero_max([0, 4, 0, 3]) == [3, 4, 3, 3]


def test_zero_max_3():
    assert zero_max([0, 1, 0]) == [1, 1, 0]


def test_zero_max_4():
    assert zero_max([0, 1, 5]) == [5, 1, 5]


def test_zero_max_5():
    assert zero_max([0, 2, 0]) == [0, 2, 0]


def test_zero_max_6():
    assert zero_max([1]) == [1]


def test_zero_max_7():
    assert zero_max([0]) == [0]


def test_zero_max_8():
    assert zero_max([]) == []


def test_zero_max_9():
    assert zero_max([7, 0, 4, 3, 0, 2]) == [7, 3, 4, 3, 0, 2]


def test_zero_max_10():
    assert zero_max([7, 0, 4, 3, 0, 1]) == [7, 3, 4, 3, 1, 1]


def test_zero_max_11():
    assert zero_max([7, 0, 4, 3, 0, 0]) == [7, 3, 4, 3, 0, 0]


def test_zero_max_12():
    assert zero_max([7, 0, 1, 0, 0, 7]) == [7, 7, 1, 7, 7, 7]
```
