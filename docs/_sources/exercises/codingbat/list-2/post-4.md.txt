# post_4





Given a non-empty list of ints, return a new list containing the elements from the original list that come after the last 4 in the original list. The original list will contain at least one 4. Note that it is valid in java to create a list of length 0.

```
post_4([2, 4, 1, 2]) -> [1, 2]
post_4([4, 1, 4, 2]) -> [2]
post_4([4, 4, 1, 2, 3]) -> [1, 2, 3]
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p164144) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def post_4(nums: List[int]) -> List[int]:
    pass


result = post_4([2, 4, 1, 2])
print(result)
```

## Tests
```python
from main import post_4


def test_post_4_1():
    assert post_4([2, 4, 1, 2]) == [1, 2]


def test_post_4_2():
    assert post_4([4, 1, 4, 2]) == [2]


def test_post_4_3():
    assert post_4([4, 4, 1, 2, 3]) == [1, 2, 3]


def test_post_4_4():
    assert post_4([4, 2]) == [2]


def test_post_4_5():
    assert post_4([4, 4, 3]) == [3]


def test_post_4_6():
    assert post_4([4, 4]) == []


def test_post_4_7():
    assert post_4([4]) == []


def test_post_4_8():
    assert post_4([2, 4, 1, 4, 3, 2]) == [3, 2]


def test_post_4_9():
    assert post_4([4, 1, 4, 2, 2, 2]) == [2, 2, 2]


def test_post_4_10():
    assert post_4([3, 4, 3, 2]) == [3, 2]
```
