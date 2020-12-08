# mod_three





Given an list of ints, return true if the list contains either 3 even or 3 odd values all next to each other.

```
mod_three([2, 1, 3, 5]) -> true
mod_three([2, 1, 2, 5]) -> false
mod_three([2, 4, 2, 5]) -> true
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p159979) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def mod_three(nums: List[int]) -> bool:
    pass


result = mod_three([2, 1, 3, 5])
print(result)
```

## Tests
```python
from main import mod_three


def test_mod_three_1():
    assert mod_three([2, 1, 3, 5]) == True


def test_mod_three_2():
    assert mod_three([2, 1, 2, 5]) == False


def test_mod_three_3():
    assert mod_three([2, 4, 2, 5]) == True


def test_mod_three_4():
    assert mod_three([1, 2, 1, 2, 1]) == False


def test_mod_three_5():
    assert mod_three([9, 9, 9]) == True


def test_mod_three_6():
    assert mod_three([1, 2, 1]) == False


def test_mod_three_7():
    assert mod_three([1, 2]) == False


def test_mod_three_8():
    assert mod_three([1]) == False


def test_mod_three_9():
    assert mod_three([]) == False


def test_mod_three_10():
    assert mod_three([9, 7, 2, 9]) == False


def test_mod_three_11():
    assert mod_three([9, 7, 2, 9, 2, 2]) == False


def test_mod_three_12():
    assert mod_three([9, 7, 2, 9, 2, 2, 6]) == True
```
