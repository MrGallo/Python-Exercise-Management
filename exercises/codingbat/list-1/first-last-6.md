# first_last_6





Given a list of ints, return true if 6 appears as either the first or last element in the list. The list will be length 1 or more.

```
first_last_6([1, 2, 6]) -> true
first_last_6([6, 1, 2, 3]) -> true
first_last_6([13, 6, 1, 2, 3]) -> false
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p185685) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def first_last_6(nums: List[int]) -> bool:
    pass


result = first_last_6([1, 2, 6])
print(result)
```

## Tests
```python
from main import first_last_6


def test_first_last_6_1():
    assert first_last_6([1, 2, 6]) == True


def test_first_last_6_2():
    assert first_last_6([6, 1, 2, 3]) == True


def test_first_last_6_3():
    assert first_last_6([13, 6, 1, 2, 3]) == False


def test_first_last_6_4():
    assert first_last_6([13, 6, 1, 2, 6]) == True


def test_first_last_6_5():
    assert first_last_6([3, 2, 1]) == False


def test_first_last_6_6():
    assert first_last_6([3, 6, 1]) == False


def test_first_last_6_7():
    assert first_last_6([3, 6]) == True


def test_first_last_6_8():
    assert first_last_6([6]) == True


def test_first_last_6_9():
    assert first_last_6([3]) == False


def test_first_last_6_10():
    assert first_last_6([5, 6]) == True


def test_first_last_6_11():
    assert first_last_6([5, 5]) == False


def test_first_last_6_12():
    assert first_last_6([1, 2, 3, 4, 6]) == True


def test_first_last_6_13():
    assert first_last_6([1, 2, 3, 4]) == False
```
