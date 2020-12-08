# without_ten





Return a version of the given list where all the 10's have been removed. The remaining elements should shift left towards the start of the list as needed, and the empty spaces a the end of the list should be 0. So {1, 10, 10, 2} yields {1, 2, 0, 0}. You may modify and return the given list or make a new list.

```
without_ten([1, 10, 10, 2]) -> [1, 2, 0, 0]
without_ten([10, 2, 10]) -> [2, 0, 0]
without_ten([1, 99, 10]) -> [1, 99, 0]
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p196976) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def without_ten(nums: List[int]) -> List[int]:
    pass


result = without_ten([1, 10, 10, 2])
print(result)
```

## Tests
```python
from main import without_ten


def test_without_ten_1():
    assert without_ten([1, 10, 10, 2]) == [1, 2, 0, 0]


def test_without_ten_2():
    assert without_ten([10, 2, 10]) == [2, 0, 0]


def test_without_ten_3():
    assert without_ten([1, 99, 10]) == [1, 99, 0]


def test_without_ten_4():
    assert without_ten([10, 13, 10, 14]) == [13, 14, 0, 0]


def test_without_ten_5():
    assert without_ten([10, 13, 10, 14, 10]) == [13, 14, 0, 0, 0]


def test_without_ten_6():
    assert without_ten([10, 10, 3]) == [3, 0, 0]


def test_without_ten_7():
    assert without_ten([1]) == [1]


def test_without_ten_8():
    assert without_ten([13, 1]) == [13, 1]


def test_without_ten_9():
    assert without_ten([10]) == [0]


def test_without_ten_10():
    assert without_ten([]) == []
```
