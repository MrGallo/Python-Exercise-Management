# middle_way





Given 2 int lists, a and b, each length 3, return a new list length 2 containing their middle elements.

```
middle_way([1, 2, 3], [4, 5, 6]) -> [2, 5]
middle_way([7, 7, 7], [3, 8, 0]) -> [7, 8]
middle_way([5, 2, 9], [1, 4, 5]) -> [2, 4]
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p146449) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def middle_way(a: List[int], b: List[int]) -> List[int]:
    pass


result = middle_way([1, 2, 3], [4, 5, 6])
print(result)
```

## Tests
```python
from main import middle_way


def test_middle_way_1():
    assert middle_way([1, 2, 3], [4, 5, 6]) == [2, 5]


def test_middle_way_2():
    assert middle_way([7, 7, 7], [3, 8, 0]) == [7, 8]


def test_middle_way_3():
    assert middle_way([5, 2, 9], [1, 4, 5]) == [2, 4]


def test_middle_way_4():
    assert middle_way([1, 9, 7], [4, 8, 8]) == [9, 8]


def test_middle_way_5():
    assert middle_way([1, 2, 3], [3, 1, 4]) == [2, 1]


def test_middle_way_6():
    assert middle_way([1, 2, 3], [4, 1, 1]) == [2, 1]
```
