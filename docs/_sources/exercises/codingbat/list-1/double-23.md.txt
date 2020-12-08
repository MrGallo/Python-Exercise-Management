# double_23





Given an int list, return true if the list contains 2 twice, or 3 twice. The list will be length 0, 1, or 2.

```
double_23([2, 2]) -> true
double_23([3, 3]) -> true
double_23([2, 3]) -> false
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p145365) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def double_23(nums: List[int]) -> bool:
    pass


result = double_23([2, 2])
print(result)
```

## Tests
```python
from main import double_23


def test_double_23_1():
    assert double_23([2, 2]) == True


def test_double_23_2():
    assert double_23([3, 3]) == True


def test_double_23_3():
    assert double_23([2, 3]) == False


def test_double_23_4():
    assert double_23([3, 2]) == False


def test_double_23_5():
    assert double_23([4, 5]) == False


def test_double_23_6():
    assert double_23([2]) == False


def test_double_23_7():
    assert double_23([3]) == False


def test_double_23_8():
    assert double_23([]) == False


def test_double_23_9():
    assert double_23([3, 4]) == False
```
