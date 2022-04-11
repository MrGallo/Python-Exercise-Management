# shift_left





Return a list that is "left shifted" by one -- so {6, 2, 5, 3} returns {2, 5, 3, 6}. You may modify and return the given list, or return a new list.

```
shift_left([6, 2, 5, 3]) -> [2, 5, 3, 6]
shift_left([1, 2]) -> [2, 1]
shift_left([1]) -> [1]
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p105031) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def shift_left(nums: List[int]) -> List[int]:
    pass


result = shift_left([6, 2, 5, 3])
print(result)
```

## Tests
```python
from main import shift_left


def test_shift_left_1():
    assert shift_left([6, 2, 5, 3]) == [2, 5, 3, 6]


def test_shift_left_2():
    assert shift_left([1, 2]) == [2, 1]


def test_shift_left_3():
    assert shift_left([1]) == [1]


def test_shift_left_4():
    assert shift_left([]) == []


def test_shift_left_5():
    assert shift_left([1, 1, 2, 2, 4]) == [1, 2, 2, 4, 1]


def test_shift_left_6():
    assert shift_left([1, 1, 1]) == [1, 1, 1]


def test_shift_left_7():
    assert shift_left([1, 2, 3]) == [2, 3, 1]
```
