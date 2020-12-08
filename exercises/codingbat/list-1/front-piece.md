# front_piece





Given an int list of any length, return a new list of its first 2 elements. If the list is smaller than length 2, use whatever elements are present.

```
front_piece([1, 2, 3]) -> [1, 2]
front_piece([1, 2]) -> [1, 2]
front_piece([1]) -> [1]
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p142455) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def front_piece(nums: List[int]) -> List[int]:
    pass


result = front_piece([1, 2, 3])
print(result)
```

## Tests
```python
from main import front_piece


def test_front_piece_1():
    assert front_piece([1, 2, 3]) == [1, 2]


def test_front_piece_2():
    assert front_piece([1, 2]) == [1, 2]


def test_front_piece_3():
    assert front_piece([1]) == [1]


def test_front_piece_4():
    assert front_piece([]) == []


def test_front_piece_5():
    assert front_piece([6, 5, 0]) == [6, 5]


def test_front_piece_6():
    assert front_piece([6, 5]) == [6, 5]


def test_front_piece_7():
    assert front_piece([3, 1, 4, 1, 5]) == [3, 1]


def test_front_piece_8():
    assert front_piece([6]) == [6]
```
