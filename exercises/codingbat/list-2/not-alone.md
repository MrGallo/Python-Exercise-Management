# not_alone





We'll say that an element in a list is "alone" if there are values before and after it, and those values are different from it. Return a version of the given list where every instance of the given value which is alone is replaced by whichever value to its left or right is larger.

```
not_alone([1, 2, 3], 2) -> [1, 3, 3]
not_alone([1, 2, 3, 2, 5, 2], 2) -> [1, 3, 3, 5, 5, 2]
not_alone([3, 4], 3) -> [3, 4]
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p169506) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def not_alone(nums: List[int], val: int) -> List[int]:
    pass


result = not_alone([1, 2, 3], 2)
print(result)
```

## Tests
```python
from main import not_alone


def test_not_alone_1():
    assert not_alone([1, 2, 3], 2) == [1, 3, 3]


def test_not_alone_2():
    assert not_alone([1, 2, 3, 2, 5, 2], 2) == [1, 3, 3, 5, 5, 2]


def test_not_alone_3():
    assert not_alone([3, 4], 3) == [3, 4]


def test_not_alone_4():
    assert not_alone([3, 3], 3) == [3, 3]


def test_not_alone_5():
    assert not_alone([1, 3, 1, 2], 1) == [1, 3, 3, 2]


def test_not_alone_6():
    assert not_alone([3], 3) == [3]


def test_not_alone_7():
    assert not_alone([], 3) == []


def test_not_alone_8():
    assert not_alone([7, 1, 6], 1) == [7, 7, 6]


def test_not_alone_9():
    assert not_alone([1, 1, 1], 1) == [1, 1, 1]


def test_not_alone_10():
    assert not_alone([1, 1, 1, 2], 1) == [1, 1, 1, 2]
```
