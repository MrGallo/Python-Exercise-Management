# swap_ends





Given a list of ints, swap the first and last elements in the list. Return the modified list. The list length will be at least 1.

```
swap_ends([1, 2, 3, 4]) -> [4, 2, 3, 1]
swap_ends([1, 2, 3]) -> [3, 2, 1]
swap_ends([8, 6, 7, 9, 5]) -> [5, 6, 7, 9, 8]
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p118044) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def swap_ends(nums: List[int]) -> List[int]:
    pass


result = swap_ends([1, 2, 3, 4])
print(result)
```

## Tests
```python
from main import swap_ends


def test_swap_ends_1():
    assert swap_ends([1, 2, 3, 4]) == [4, 2, 3, 1]


def test_swap_ends_2():
    assert swap_ends([1, 2, 3]) == [3, 2, 1]


def test_swap_ends_3():
    assert swap_ends([8, 6, 7, 9, 5]) == [5, 6, 7, 9, 8]


def test_swap_ends_4():
    assert swap_ends([3, 1, 4, 1, 5, 9]) == [9, 1, 4, 1, 5, 3]


def test_swap_ends_5():
    assert swap_ends([1, 2]) == [2, 1]


def test_swap_ends_6():
    assert swap_ends([1]) == [1]
```
