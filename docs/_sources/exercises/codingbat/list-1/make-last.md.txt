# make_last





Given an int list, return a new list with double the length where its last element is the same as the original list, and all the other elements are 0. The original list will be length 1 or more. Note: by default, a new int list contains all 0's.

```
make_last([4, 5, 6]) -> [0, 0, 0, 0, 0, 6]
make_last([1, 2]) -> [0, 0, 0, 2]
make_last([3]) -> [0, 3]
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p137188) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def make_last(nums: List[int]) -> List[int]:
    pass


result = make_last([4, 5, 6])
print(result)
```

## Tests
```python
from main import make_last


def test_make_last_1():
    assert make_last([4, 5, 6]) == [0, 0, 0, 0, 0, 6]


def test_make_last_2():
    assert make_last([1, 2]) == [0, 0, 0, 2]


def test_make_last_3():
    assert make_last([3]) == [0, 3]


def test_make_last_4():
    assert make_last([0]) == [0, 0]


def test_make_last_5():
    assert make_last([7, 7, 7]) == [0, 0, 0, 0, 0, 7]


def test_make_last_6():
    assert make_last([3, 1, 4]) == [0, 0, 0, 0, 0, 4]


def test_make_last_7():
    assert make_last([1, 2, 3, 4]) == [0, 0, 0, 0, 0, 0, 0, 4]


def test_make_last_8():
    assert make_last([1, 2, 3, 0]) == [0, 0, 0, 0, 0, 0, 0, 0]


def test_make_last_9():
    assert make_last([2, 4]) == [0, 0, 0, 4]
```
