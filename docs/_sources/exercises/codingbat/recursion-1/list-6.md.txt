# list_6





Given a list of ints, compute recursively if the list contains a `6`. We'll use the convention of considering only the part of the list that begins at the given index. In this way, a recursive call can pass `index + 1` to move down the list. The initial call will pass in index as `0`.

```
list_6([1, 6, 4], 0) -> true
list_6([1, 4], 0) -> false
list_6([6], 0) -> true
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p108997) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def list_6(nums: List[int], index: int) -> bool:
    pass


result = list_6([1, 6, 4], 0)
print(result)
```

## Tests
```python
from main import list_6


def test_list_6_1():
    assert list_6([1, 6, 4], 0) == True


def test_list_6_2():
    assert list_6([1, 4], 0) == False


def test_list_6_3():
    assert list_6([6], 0) == True


def test_list_6_4():
    assert list_6([], 0) == False


def test_list_6_5():
    assert list_6([6, 2, 2], 0) == True


def test_list_6_6():
    assert list_6([2, 5], 0) == False


def test_list_6_7():
    assert list_6([1, 9, 4, 6, 6], 0) == True


def test_list_6_8():
    assert list_6([2, 5, 6], 0) == True
```
