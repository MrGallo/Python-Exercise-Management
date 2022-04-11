# sum_28





Given a list of ints, return true if the sum of all the 2's in the list is exactly 8.

```
sum_28([2, 3, 2, 2, 4, 2]) -> true
sum_28([2, 3, 2, 2, 4, 2, 2]) -> false
sum_28([1, 2, 3, 4]) -> false
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p199612) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def sum_28(nums: List[int]) -> bool:
    pass


result = sum_28([2, 3, 2, 2, 4, 2])
print(result)
```

## Tests
```python
from main import sum_28


def test_sum_28_1():
    assert sum_28([2, 3, 2, 2, 4, 2]) == True


def test_sum_28_2():
    assert sum_28([2, 3, 2, 2, 4, 2, 2]) == False


def test_sum_28_3():
    assert sum_28([1, 2, 3, 4]) == False


def test_sum_28_4():
    assert sum_28([2, 2, 2, 2]) == True


def test_sum_28_5():
    assert sum_28([1, 2, 2, 2, 2, 4]) == True


def test_sum_28_6():
    assert sum_28([]) == False


def test_sum_28_7():
    assert sum_28([2]) == False


def test_sum_28_8():
    assert sum_28([8]) == False


def test_sum_28_9():
    assert sum_28([2, 2, 2]) == False


def test_sum_28_10():
    assert sum_28([2, 2, 2, 2, 2]) == False


def test_sum_28_11():
    assert sum_28([1, 2, 2, 1, 2, 2]) == True


def test_sum_28_12():
    assert sum_28([5, 2, 2, 2, 4, 2]) == True
```
