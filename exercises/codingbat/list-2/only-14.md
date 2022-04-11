# only_14





Given a list of ints, return true if every element is a 1 or a 4.

```
only_14([1, 4, 1, 4]) -> true
only_14([1, 4, 2, 4]) -> false
only_14([1, 1]) -> true
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p186672) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def only_14(nums: List[int]) -> bool:
    pass


result = only_14([1, 4, 1, 4])
print(result)
```

## Tests
```python
from main import only_14


def test_only_14_1():
    assert only_14([1, 4, 1, 4]) == True


def test_only_14_2():
    assert only_14([1, 4, 2, 4]) == False


def test_only_14_3():
    assert only_14([1, 1]) == True


def test_only_14_4():
    assert only_14([4, 1]) == True


def test_only_14_5():
    assert only_14([2]) == False


def test_only_14_6():
    assert only_14([]) == True


def test_only_14_7():
    assert only_14([1, 4, 1, 3]) == False


def test_only_14_8():
    assert only_14([3, 1, 3]) == False


def test_only_14_9():
    assert only_14([1]) == True


def test_only_14_10():
    assert only_14([4]) == True


def test_only_14_11():
    assert only_14([3, 4]) == False


def test_only_14_12():
    assert only_14([1, 3, 4]) == False


def test_only_14_13():
    assert only_14([1, 1, 1]) == True


def test_only_14_14():
    assert only_14([1, 1, 1, 5]) == False


def test_only_14_15():
    assert only_14([4, 1, 4, 1]) == True
```
