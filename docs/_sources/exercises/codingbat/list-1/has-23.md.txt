# has_23





Given an int list length 2, return true if it contains a 2 or a 3.

```
has_23([2, 5]) -> true
has_23([4, 3]) -> true
has_23([4, 5]) -> false
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p171022) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def has_23(nums: List[int]) -> bool:
    pass


result = has_23([2, 5])
print(result)
```

## Tests
```python
from main import has_23


def test_has_23_1():
    assert has_23([2, 5]) == True


def test_has_23_2():
    assert has_23([4, 3]) == True


def test_has_23_3():
    assert has_23([4, 5]) == False


def test_has_23_4():
    assert has_23([2, 2]) == True


def test_has_23_5():
    assert has_23([3, 2]) == True


def test_has_23_6():
    assert has_23([3, 3]) == True


def test_has_23_7():
    assert has_23([7, 7]) == False


def test_has_23_8():
    assert has_23([3, 9]) == True


def test_has_23_9():
    assert has_23([9, 5]) == False
```
