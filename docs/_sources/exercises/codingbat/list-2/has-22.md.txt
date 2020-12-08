# has_22





Given an list of ints, return true if the list contains a 2 next to a 2 somewhere.

```
has_22([1, 2, 2]) -> true
has_22([1, 2, 1, 2]) -> false
has_22([2, 1, 2]) -> false
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p121853) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def has_22(nums: List[int]) -> bool:
    pass


result = has_22([1, 2, 2])
print(result)
```

## Tests
```python
from main import has_22


def test_has_22_1():
    assert has_22([1, 2, 2]) == True


def test_has_22_2():
    assert has_22([1, 2, 1, 2]) == False


def test_has_22_3():
    assert has_22([2, 1, 2]) == False


def test_has_22_4():
    assert has_22([2, 2, 1, 2]) == True


def test_has_22_5():
    assert has_22([1, 3, 2]) == False


def test_has_22_6():
    assert has_22([1, 3, 2, 2]) == True


def test_has_22_7():
    assert has_22([2, 3, 2, 2]) == True


def test_has_22_8():
    assert has_22([4, 2, 4, 2, 2, 5]) == True


def test_has_22_9():
    assert has_22([1, 2]) == False


def test_has_22_10():
    assert has_22([2, 2]) == True


def test_has_22_11():
    assert has_22([2]) == False


def test_has_22_12():
    assert has_22([]) == False


def test_has_22_13():
    assert has_22([3, 3, 2, 2]) == True


def test_has_22_14():
    assert has_22([5, 2, 5, 2]) == False
```
