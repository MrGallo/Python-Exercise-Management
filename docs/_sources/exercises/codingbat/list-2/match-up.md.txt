# match_up





Given lists nums1 and nums2 of the same length, for every element in nums1, consider the corresponding element in nums2 (at the same index). Return the count of the number of times that the two elements differ by 2 or less, but are not equal.

```
match_up([1, 2, 3], [2, 3, 10]) -> 2
match_up([1, 2, 3], [2, 3, 5]) -> 3
match_up([1, 2, 3], [2, 3, 3]) -> 2
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p136254) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def match_up(nums_1: List[int], nums_2: List[int]) -> int:
    pass


result = match_up([1, 2, 3], [2, 3, 10])
print(result)
```

## Tests
```python
from main import match_up


def test_match_up_1():
    assert match_up([1, 2, 3], [2, 3, 10]) == 2


def test_match_up_2():
    assert match_up([1, 2, 3], [2, 3, 5]) == 3


def test_match_up_3():
    assert match_up([1, 2, 3], [2, 3, 3]) == 2


def test_match_up_4():
    assert match_up([5, 3], [5, 5]) == 1


def test_match_up_5():
    assert match_up([5, 3], [4, 4]) == 2


def test_match_up_6():
    assert match_up([5, 3], [3, 3]) == 1


def test_match_up_7():
    assert match_up([5, 3], [2, 2]) == 1


def test_match_up_8():
    assert match_up([5, 3], [1, 1]) == 1


def test_match_up_9():
    assert match_up([5, 3], [0, 0]) == 0


def test_match_up_10():
    assert match_up([4], [4]) == 0


def test_match_up_11():
    assert match_up([4], [5]) == 1
```
