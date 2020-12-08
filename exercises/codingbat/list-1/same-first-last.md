# same_first_last





Given an list of ints, return true if the list is length 1 or more, and the first element and the last element are equal.

```
same_first_last([1, 2, 3]) -> false
same_first_last([1, 2, 3, 1]) -> true
same_first_last([1, 2, 1]) -> true
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p118976) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def same_first_last(nums: List[int]) -> bool:
    pass


result = same_first_last([1, 2, 3])
print(result)
```

## Tests
```python
from main import same_first_last


def test_same_first_last_1():
    assert same_first_last([1, 2, 3]) == False


def test_same_first_last_2():
    assert same_first_last([1, 2, 3, 1]) == True


def test_same_first_last_3():
    assert same_first_last([1, 2, 1]) == True


def test_same_first_last_4():
    assert same_first_last([7]) == True


def test_same_first_last_5():
    assert same_first_last([]) == False


def test_same_first_last_6():
    assert same_first_last([1, 2, 3, 4, 5, 1]) == True


def test_same_first_last_7():
    assert same_first_last([1, 2, 3, 4, 5, 13]) == False


def test_same_first_last_8():
    assert same_first_last([13, 2, 3, 4, 5, 13]) == True


def test_same_first_last_9():
    assert same_first_last([7, 7]) == True
```
