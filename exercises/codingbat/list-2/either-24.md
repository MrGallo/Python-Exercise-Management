# either_24





Given a list of ints, return true if the list contains a 2 next to a 2 or a 4 next to a 4, but not both.

```
either_24([1, 2, 2]) -> true
either_24([4, 4, 1]) -> true
either_24([4, 4, 1, 2, 2]) -> false
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p191878) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def either_24(nums: List[int]) -> bool:
    pass


result = either_24([1, 2, 2])
print(result)
```

## Tests
```python
from main import either_24


def test_either_24_1():
    assert either_24([1, 2, 2]) == True


def test_either_24_2():
    assert either_24([4, 4, 1]) == True


def test_either_24_3():
    assert either_24([4, 4, 1, 2, 2]) == False


def test_either_24_4():
    assert either_24([1, 2, 3, 4]) == False


def test_either_24_5():
    assert either_24([3, 5, 9]) == False


def test_either_24_6():
    assert either_24([1, 2, 3, 4, 4]) == True


def test_either_24_7():
    assert either_24([2, 2, 3, 4]) == True


def test_either_24_8():
    assert either_24([1, 2, 3, 2, 2, 4]) == True


def test_either_24_9():
    assert either_24([1, 2, 3, 2, 2, 4, 4]) == False


def test_either_24_10():
    assert either_24([1, 2]) == False


def test_either_24_11():
    assert either_24([2, 2]) == True


def test_either_24_12():
    assert either_24([4, 4]) == True


def test_either_24_13():
    assert either_24([2]) == False


def test_either_24_14():
    assert either_24([]) == False
```
