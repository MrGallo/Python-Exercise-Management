# max_triple





Given a list of ints of odd length, look at the first, last, and middle values in the list and return the largest. The list length will be a least 1.

```
max_triple([1, 2, 3]) -> 3
max_triple([1, 5, 3]) -> 5
max_triple([5, 2, 3]) -> 5
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p185176) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def max_triple(nums: List[int]) -> int:
    pass


result = max_triple([1, 2, 3])
print(result)
```

## Tests
```python
from main import max_triple


def test_max_triple_1():
    assert max_triple([1, 2, 3]) == 3


def test_max_triple_2():
    assert max_triple([1, 5, 3]) == 5


def test_max_triple_3():
    assert max_triple([5, 2, 3]) == 5


def test_max_triple_4():
    assert max_triple([1, 2, 3, 1, 1]) == 3


def test_max_triple_5():
    assert max_triple([1, 7, 3, 1, 5]) == 5


def test_max_triple_6():
    assert max_triple([5, 1, 3, 7, 1]) == 5


def test_max_triple_7():
    assert max_triple([5, 1, 7, 3, 7, 8, 1]) == 5


def test_max_triple_8():
    assert max_triple([5, 1, 7, 9, 7, 8, 1]) == 9


def test_max_triple_9():
    assert max_triple([5, 1, 7, 3, 7, 8, 9]) == 9


def test_max_triple_10():
    assert max_triple([2, 2, 5, 1, 1]) == 5
```
