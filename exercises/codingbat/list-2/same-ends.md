# same_ends





Return true if the group of N numbers at the start and end of the list are the same. For example, with {5, 6, 45, 99, 13, 5, 6}, the ends are the same for n=0 and n=2, and false for n=1 and n=3. You may assume that n is in the range 0..nums.length inclusive.

```
same_ends([5, 6, 45, 99, 13, 5, 6], 1) -> false
same_ends([5, 6, 45, 99, 13, 5, 6], 2) -> true
same_ends([5, 6, 45, 99, 13, 5, 6], 3) -> false
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p134300) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def same_ends(nums: List[int], len: int) -> bool:
    pass


result = same_ends([5, 6, 45, 99, 13, 5, 6], 1)
print(result)
```

## Tests
```python
from main import same_ends


def test_same_ends_1():
    assert same_ends([5, 6, 45, 99, 13, 5, 6], 1) == False


def test_same_ends_2():
    assert same_ends([5, 6, 45, 99, 13, 5, 6], 2) == True


def test_same_ends_3():
    assert same_ends([5, 6, 45, 99, 13, 5, 6], 3) == False


def test_same_ends_4():
    assert same_ends([1, 2, 5, 2, 1], 1) == True


def test_same_ends_5():
    assert same_ends([1, 2, 5, 2, 1], 2) == False


def test_same_ends_6():
    assert same_ends([1, 2, 5, 2, 1], 0) == True


def test_same_ends_7():
    assert same_ends([1, 2, 5, 2, 1], 5) == True


def test_same_ends_8():
    assert same_ends([1, 1, 1], 0) == True


def test_same_ends_9():
    assert same_ends([1, 1, 1], 1) == True


def test_same_ends_10():
    assert same_ends([1, 1, 1], 2) == True


def test_same_ends_11():
    assert same_ends([1, 1, 1], 3) == True


def test_same_ends_12():
    assert same_ends([1], 1) == True


def test_same_ends_13():
    assert same_ends([], 0) == True


def test_same_ends_14():
    assert same_ends([4, 2, 4, 5], 1) == False
```
