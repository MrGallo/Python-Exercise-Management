# lucky_13





Given a list of ints, return true if the list contains no 1's and no 3's.

```
lucky_13([0, 2, 4]) -> true
lucky_13([1, 2, 3]) -> false
lucky_13([1, 2, 4]) -> false
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p194525) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def lucky_13(nums: List[int]) -> bool:
    pass


result = lucky_13([0, 2, 4])
print(result)
```

## Tests
```python
from main import lucky_13


def test_lucky_13_1():
    assert lucky_13([0, 2, 4]) == True


def test_lucky_13_2():
    assert lucky_13([1, 2, 3]) == False


def test_lucky_13_3():
    assert lucky_13([1, 2, 4]) == False


def test_lucky_13_4():
    assert lucky_13([2, 7, 2, 8]) == True


def test_lucky_13_5():
    assert lucky_13([2, 7, 1, 8]) == False


def test_lucky_13_6():
    assert lucky_13([3, 7, 2, 8]) == False


def test_lucky_13_7():
    assert lucky_13([2, 7, 2, 1]) == False


def test_lucky_13_8():
    assert lucky_13([1, 2]) == False


def test_lucky_13_9():
    assert lucky_13([2, 2]) == True


def test_lucky_13_10():
    assert lucky_13([2]) == True


def test_lucky_13_11():
    assert lucky_13([3]) == False


def test_lucky_13_12():
    assert lucky_13([]) == True
```
