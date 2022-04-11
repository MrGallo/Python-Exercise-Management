# pre_4





Given a non-empty list of ints, return a new list containing the elements from the original list that come before the first 4 in the original list. The original list will contain at least one 4. Note that it is valid in java to create a list of length 0.

```
pre_4([1, 2, 4, 1]) -> [1, 2]
pre_4([3, 1, 4]) -> [3, 1]
pre_4([1, 4, 4]) -> [1]
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p100246) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def pre_4(nums: List[int]) -> List[int]:
    pass


result = pre_4([1, 2, 4, 1])
print(result)
```

## Tests
```python
from main import pre_4


def test_pre_4_1():
    assert pre_4([1, 2, 4, 1]) == [1, 2]


def test_pre_4_2():
    assert pre_4([3, 1, 4]) == [3, 1]


def test_pre_4_3():
    assert pre_4([1, 4, 4]) == [1]


def test_pre_4_4():
    assert pre_4([1, 4, 4, 2]) == [1]


def test_pre_4_5():
    assert pre_4([1, 3, 4, 2, 4]) == [1, 3]


def test_pre_4_6():
    assert pre_4([4, 4]) == []


def test_pre_4_7():
    assert pre_4([3, 3, 4]) == [3, 3]


def test_pre_4_8():
    assert pre_4([1, 2, 1, 4]) == [1, 2, 1]


def test_pre_4_9():
    assert pre_4([2, 1, 4, 2]) == [2, 1]


def test_pre_4_10():
    assert pre_4([2, 1, 2, 1, 4, 2]) == [2, 1, 2, 1]
```
