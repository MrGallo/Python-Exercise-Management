# make_ends





Given a list of ints, return a new list length 2 containing the first and last elements from the original list. The original list will be length 1 or more.

```
make_ends([1, 2, 3]) -> [1, 3]
make_ends([1, 2, 3, 4]) -> [1, 4]
make_ends([7, 4, 6, 2]) -> [7, 2]
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p101230) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def make_ends(nums: List[int]) -> List[int]:
    pass


result = make_ends([1, 2, 3])
print(result)
```

## Tests
```python
from main import make_ends


def test_make_ends_1():
    assert make_ends([1, 2, 3]) == [1, 3]


def test_make_ends_2():
    assert make_ends([1, 2, 3, 4]) == [1, 4]


def test_make_ends_3():
    assert make_ends([7, 4, 6, 2]) == [7, 2]


def test_make_ends_4():
    assert make_ends([1, 2, 2, 2, 2, 2, 2, 3]) == [1, 3]


def test_make_ends_5():
    assert make_ends([7, 4]) == [7, 4]


def test_make_ends_6():
    assert make_ends([7]) == [7, 7]


def test_make_ends_7():
    assert make_ends([5, 2, 9]) == [5, 9]


def test_make_ends_8():
    assert make_ends([2, 3, 4, 1]) == [2, 1]
```
