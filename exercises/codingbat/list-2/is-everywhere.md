# is_everywhere





We'll say that a value is "everywhere" in a list if for every pair of adjacent elements in the list, at least one of the pair is that value. Return true if the given value is everywhere in the list.

```
is_everywhere([1, 2, 1, 3], 1) -> true
is_everywhere([1, 2, 1, 3], 2) -> false
is_everywhere([1, 2, 1, 3, 4], 1) -> false
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p110222) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def is_everywhere(nums: List[int], val: int) -> bool:
    pass


result = is_everywhere([1, 2, 1, 3], 1)
print(result)
```

## Tests
```python
from main import is_everywhere


def test_is_everywhere_1():
    assert is_everywhere([1, 2, 1, 3], 1) == True


def test_is_everywhere_2():
    assert is_everywhere([1, 2, 1, 3], 2) == False


def test_is_everywhere_3():
    assert is_everywhere([1, 2, 1, 3, 4], 1) == False


def test_is_everywhere_4():
    assert is_everywhere([2, 1, 2, 1], 1) == True


def test_is_everywhere_5():
    assert is_everywhere([2, 1, 2, 1], 2) == True


def test_is_everywhere_6():
    assert is_everywhere([2, 1, 2, 3, 1], 2) == False


def test_is_everywhere_7():
    assert is_everywhere([3, 1], 3) == True


def test_is_everywhere_8():
    assert is_everywhere([3, 1], 2) == False


def test_is_everywhere_9():
    assert is_everywhere([3], 1) == True


def test_is_everywhere_10():
    assert is_everywhere([], 1) == True


def test_is_everywhere_11():
    assert is_everywhere([1, 2, 1, 2, 3, 2, 5], 2) == True


def test_is_everywhere_12():
    assert is_everywhere([1, 2, 1, 1, 1, 2], 2) == False


def test_is_everywhere_13():
    assert is_everywhere([2, 1, 2, 1, 1, 2], 2) == False


def test_is_everywhere_14():
    assert is_everywhere([2, 1, 2, 2, 2, 1, 1, 2], 2) == False


def test_is_everywhere_15():
    assert is_everywhere([2, 1, 2, 2, 2, 1, 2, 1], 2) == True


def test_is_everywhere_16():
    assert is_everywhere([2, 1, 2, 1, 2], 2) == True
```
