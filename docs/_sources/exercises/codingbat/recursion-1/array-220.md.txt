# array_220





Given an list of ints, compute recursively if the list contains somewhere a value followed in the list by that value times 10. We'll use the convention of considering only the part of the list that begins at the given index. In this way, a recursive call can pass index+1 to move down the list. The initial call will pass in index as 0.

```
list220([1, 2, 20], 0) -> true
list220([3, 30], 0) -> true
list220([3], 0) -> false
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p173469) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def array_220(nums: List[int], index: int) -> bool:
    pass


result = array_220([1, 2, 20], 0)
print(result)
```

## Tests
```python
from main import array_220


def test_array_220_1():
    assert array_220([1, 2, 20], 0) == True


def test_array_220_2():
    assert array_220([3, 30], 0) == True


def test_array_220_3():
    assert array_220([3], 0) == False


def test_array_220_4():
    assert array_220([], 0) == False


def test_array_220_5():
    assert array_220([3, 3, 30, 4], 0) == True


def test_array_220_6():
    assert array_220([2, 19, 4], 0) == False


def test_array_220_7():
    assert array_220([20, 2, 21], 0) == False


def test_array_220_8():
    assert array_220([20, 2, 21, 210], 0) == True


def test_array_220_9():
    assert array_220([2, 200, 2000], 0) == True


def test_array_220_10():
    assert array_220([0, 0], 0) == True


def test_array_220_11():
    assert array_220([1, 2, 3, 4, 5, 6], 0) == False


def test_array_220_12():
    assert array_220([1, 2, 3, 4, 5, 50, 6], 0) == True


def test_array_220_13():
    assert array_220([1, 2, 3, 4, 5, 51, 6], 0) == False


def test_array_220_14():
    assert array_220([1, 2, 3, 4, 4, 50, 500, 6], 0) == True
```
