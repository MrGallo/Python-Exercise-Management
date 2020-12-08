# front_11





Given 2 int lists, a and b, of any length, return a new list with the first element of each list. If either list is length 0, ignore that list.

```
front_11([1, 2, 3], [7, 9, 8]) -> [1, 7]
front_11([1], [2]) -> [1, 2]
front_11([1, 7], []) -> [1]
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p128270) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def front_11(a: List[int], b: List[int]) -> List[int]:
    pass


result = front_11([1, 2, 3], [7, 9, 8])
print(result)
```

## Tests
```python
from main import front_11


def test_front_11_1():
    assert front_11([1, 2, 3], [7, 9, 8]) == [1, 7]


def test_front_11_2():
    assert front_11([1], [2]) == [1, 2]


def test_front_11_3():
    assert front_11([1, 7], []) == [1]


def test_front_11_4():
    assert front_11([], [2, 8]) == [2]


def test_front_11_5():
    assert front_11([], []) == []


def test_front_11_6():
    assert front_11([3], [1, 4, 1, 9]) == [3, 1]


def test_front_11_7():
    assert front_11([1, 4, 1, 9], []) == [1]
```
