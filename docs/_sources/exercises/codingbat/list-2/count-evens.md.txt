# count_evens



**Requirements:**
```eval_rst
- :ref:`fundamentals:mathematical operations`
- :ref:`fundamentals:loop through a list (for)`
- :ref:`fundamentals:loop with an accumulator variable`

```


Return the number of even ints in the given list. Note: the `%` "mod" operator computes the remainder, e.g. `5 % 2` is `1`.

```
count_evens([2, 1, 2, 3, 4]) -> 3
count_evens([2, 2, 0]) -> 3
count_evens([1, 3, 5]) -> 0
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p162010) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def count_evens(nums: List[int]) -> int:
    pass


result = count_evens([2, 1, 2, 3, 4])
print(result)
```

## Tests
```python
from main import count_evens


def test_count_evens_1():
    assert count_evens([2, 1, 2, 3, 4]) == 3


def test_count_evens_2():
    assert count_evens([2, 2, 0]) == 3


def test_count_evens_3():
    assert count_evens([1, 3, 5]) == 0


def test_count_evens_4():
    assert count_evens([]) == 0


def test_count_evens_5():
    assert count_evens([11, 9, 0, 1]) == 1


def test_count_evens_6():
    assert count_evens([2, 11, 9, 0]) == 2


def test_count_evens_7():
    assert count_evens([2]) == 1


def test_count_evens_8():
    assert count_evens([2, 5, 12]) == 2
```
