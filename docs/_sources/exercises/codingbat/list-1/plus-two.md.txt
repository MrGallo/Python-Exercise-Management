# plus_two





Given 2 int lists, each length 2, return a new list length 4 containing all their elements.

```
plus_two([1, 2], [3, 4]) -> [1, 2, 3, 4]
plus_two([4, 4], [2, 2]) -> [4, 4, 2, 2]
plus_two([9, 2], [3, 4]) -> [9, 2, 3, 4]
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p180840) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def plus_two(a: List[int], b: List[int]) -> List[int]:
    pass


result = plus_two([1, 2], [3, 4])
print(result)
```

## Tests
```python
from main import plus_two


def test_plus_two_1():
    assert plus_two([1, 2], [3, 4]) == [1, 2, 3, 4]


def test_plus_two_2():
    assert plus_two([4, 4], [2, 2]) == [4, 4, 2, 2]


def test_plus_two_3():
    assert plus_two([9, 2], [3, 4]) == [9, 2, 3, 4]
```
