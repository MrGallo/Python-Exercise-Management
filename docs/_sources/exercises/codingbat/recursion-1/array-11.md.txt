# array_11





Given an list of ints, compute recursively the number of times that the value 11 appears in the list. We'll use the convention of considering only the part of the list that begins at the given index. In this way, a recursive call can pass index+1 to move down the list. The initial call will pass in index as 0.

```
list11([1, 2, 11], 0) -> 1
list11([11, 11], 0) -> 2
list11([1, 2, 3, 4], 0) -> 0
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p135988) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def array_11(nums: List[int], index: int) -> int:
    pass


result = array_11([1, 2, 11], 0)
print(result)
```

## Tests
```python
from main import array_11


def test_array_11_1():
    assert array_11([1, 2, 11], 0) == 1


def test_array_11_2():
    assert array_11([11, 11], 0) == 2


def test_array_11_3():
    assert array_11([1, 2, 3, 4], 0) == 0


def test_array_11_4():
    assert array_11([1, 11, 3, 11, 11], 0) == 3


def test_array_11_5():
    assert array_11([11], 0) == 1


def test_array_11_6():
    assert array_11([1], 0) == 0


def test_array_11_7():
    assert array_11([], 0) == 0


def test_array_11_8():
    assert array_11([11, 2, 3, 4, 11, 5], 0) == 2


def test_array_11_9():
    assert array_11([11, 5, 11], 0) == 2
```
