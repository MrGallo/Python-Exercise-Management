# sum_2





Given a list of ints, return the sum of the first 2 elements in the list. If the list length is less than 2, just sum up the elements that exist, returning 0 if the list is length 0.

```
sum_2([1, 2, 3]) -> 3
sum_2([1, 1]) -> 2
sum_2([1, 1, 1, 1]) -> 2
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p190968) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def sum_2(nums: List[int]) -> int:
    pass


result = sum_2([1, 2, 3])
print(result)
```

## Tests
```python
from main import sum_2


def test_sum_2_1():
    assert sum_2([1, 2, 3]) == 3


def test_sum_2_2():
    assert sum_2([1, 1]) == 2


def test_sum_2_3():
    assert sum_2([1, 1, 1, 1]) == 2


def test_sum_2_4():
    assert sum_2([1, 2]) == 3


def test_sum_2_5():
    assert sum_2([1]) == 1


def test_sum_2_6():
    assert sum_2([]) == 0


def test_sum_2_7():
    assert sum_2([4, 5, 6]) == 9


def test_sum_2_8():
    assert sum_2([4]) == 4
```
