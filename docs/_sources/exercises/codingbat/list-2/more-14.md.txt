# more_14





Given a list of ints, return true if the number of 1's is greater than the number of 4's

```
more_14([1, 4, 1]) -> true
more_14([1, 4, 1, 4]) -> false
more_14([1, 1]) -> true
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p104627) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def more_14(nums: List[int]) -> bool:
    pass


result = more_14([1, 4, 1])
print(result)
```

## Tests
```python
from main import more_14


def test_more_14_1():
    assert more_14([1, 4, 1]) == True


def test_more_14_2():
    assert more_14([1, 4, 1, 4]) == False


def test_more_14_3():
    assert more_14([1, 1]) == True


def test_more_14_4():
    assert more_14([1, 6, 6]) == True


def test_more_14_5():
    assert more_14([1]) == True


def test_more_14_6():
    assert more_14([1, 4]) == False


def test_more_14_7():
    assert more_14([6, 1, 1]) == True


def test_more_14_8():
    assert more_14([1, 6, 4]) == False


def test_more_14_9():
    assert more_14([1, 1, 4, 4, 1]) == True


def test_more_14_10():
    assert more_14([1, 1, 6, 4, 4, 1]) == True


def test_more_14_11():
    assert more_14([]) == False


def test_more_14_12():
    assert more_14([4, 1, 4, 6]) == False


def test_more_14_13():
    assert more_14([4, 1, 4, 6, 1]) == False


def test_more_14_14():
    assert more_14([1, 4, 1, 4, 1, 6]) == True
```
