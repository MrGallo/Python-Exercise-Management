# two_two





Given a list of ints, return true if every 2 that appears in the list is next to another 2.

```
two_two([4, 2, 2, 3]) -> true
two_two([2, 2, 4]) -> true
two_two([2, 2, 4, 2]) -> false
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p102145) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def two_two(nums: List[int]) -> bool:
    pass


result = two_two([4, 2, 2, 3])
print(result)
```

## Tests
```python
from main import two_two


def test_two_two_1():
    assert two_two([4, 2, 2, 3]) == True


def test_two_two_2():
    assert two_two([2, 2, 4]) == True


def test_two_two_3():
    assert two_two([2, 2, 4, 2]) == False


def test_two_two_4():
    assert two_two([1, 3, 4]) == True


def test_two_two_5():
    assert two_two([1, 2, 2, 3, 4]) == True


def test_two_two_6():
    assert two_two([1, 2, 3, 4]) == False


def test_two_two_7():
    assert two_two([2, 2]) == True


def test_two_two_8():
    assert two_two([2, 2, 7]) == True


def test_two_two_9():
    assert two_two([2, 2, 7, 2, 1]) == False


def test_two_two_10():
    assert two_two([4, 2, 2, 2]) == True


def test_two_two_11():
    assert two_two([2, 2, 2]) == True


def test_two_two_12():
    assert two_two([1, 2]) == False


def test_two_two_13():
    assert two_two([2]) == False


def test_two_two_14():
    assert two_two([1]) == True


def test_two_two_15():
    assert two_two([]) == True


def test_two_two_16():
    assert two_two([5, 2, 2, 3]) == True


def test_two_two_17():
    assert two_two([2, 2, 5, 2]) == False
```
