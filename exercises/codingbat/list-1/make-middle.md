# make_middle





Given an list of ints of even length, return a new list length 2 containing the middle two elements from the original list. The original list will be length 2 or more.

```
make_middle([1, 2, 3, 4]) -> [2, 3]
make_middle([7, 1, 2, 3, 4, 9]) -> [2, 3]
make_middle([1, 2]) -> [1, 2]
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p199519) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def make_middle(nums: List[int]) -> List[int]:
    pass


result = make_middle([1, 2, 3, 4])
print(result)
```

## Tests
```python
from main import make_middle


def test_make_middle_1():
    assert make_middle([1, 2, 3, 4]) == [2, 3]


def test_make_middle_2():
    assert make_middle([7, 1, 2, 3, 4, 9]) == [2, 3]


def test_make_middle_3():
    assert make_middle([1, 2]) == [1, 2]


def test_make_middle_4():
    assert make_middle([5, 2, 4, 7]) == [2, 4]


def test_make_middle_5():
    assert make_middle([9, 0, 4, 3, 9, 1]) == [4, 3]
```
