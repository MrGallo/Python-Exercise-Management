# have_three





Given a list of ints, return true if the value 3 appears in the list exactly 3 times, and no 3's are next to each other.

```
have_three([3, 1, 3, 1, 3]) -> true
have_three([3, 1, 3, 3]) -> false
have_three([3, 4, 3, 3, 4]) -> false
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p109783) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def have_three(nums: List[int]) -> bool:
    pass


result = have_three([3, 1, 3, 1, 3])
print(result)
```

## Tests
```python
from main import have_three


def test_have_three_1():
    assert have_three([3, 1, 3, 1, 3]) == True


def test_have_three_2():
    assert have_three([3, 1, 3, 3]) == False


def test_have_three_3():
    assert have_three([3, 4, 3, 3, 4]) == False


def test_have_three_4():
    assert have_three([1, 3, 1, 3, 1, 2]) == False


def test_have_three_5():
    assert have_three([1, 3, 1, 3, 1, 3]) == True


def test_have_three_6():
    assert have_three([1, 3, 3, 1, 3]) == False


def test_have_three_7():
    assert have_three([1, 3, 1, 3, 1, 3, 4, 3]) == False


def test_have_three_8():
    assert have_three([3, 4, 3, 4, 3, 4, 4]) == True


def test_have_three_9():
    assert have_three([3, 3, 3]) == False


def test_have_three_10():
    assert have_three([1, 3]) == False


def test_have_three_11():
    assert have_three([3]) == False


def test_have_three_12():
    assert have_three([1]) == False
```
