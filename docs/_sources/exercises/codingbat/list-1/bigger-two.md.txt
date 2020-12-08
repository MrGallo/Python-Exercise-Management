# bigger_two





Start with 2 int lists, a and b, each length 2. Consider the sum of the values in each list. Return the list which has the largest sum. In event of a tie, return a.

```
bigger_two([1, 2], [3, 4]) -> [3, 4]
bigger_two([3, 4], [1, 2]) -> [3, 4]
bigger_two([1, 1], [1, 2]) -> [1, 2]
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p109537) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def bigger_two(a: List[int], b: List[int]) -> List[int]:
    pass


result = bigger_two([1, 2], [3, 4])
print(result)
```

## Tests
```python
from main import bigger_two


def test_bigger_two_1():
    assert bigger_two([1, 2], [3, 4]) == [3, 4]


def test_bigger_two_2():
    assert bigger_two([3, 4], [1, 2]) == [3, 4]


def test_bigger_two_3():
    assert bigger_two([1, 1], [1, 2]) == [1, 2]


def test_bigger_two_4():
    assert bigger_two([2, 1], [1, 1]) == [2, 1]


def test_bigger_two_5():
    assert bigger_two([2, 2], [1, 3]) == [2, 2]


def test_bigger_two_6():
    assert bigger_two([1, 3], [2, 2]) == [1, 3]


def test_bigger_two_7():
    assert bigger_two([6, 7], [3, 1]) == [6, 7]
```
