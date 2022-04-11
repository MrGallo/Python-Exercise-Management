# reverse_3





Given a list of ints length 3, return a new list with the elements in reverse order, so `[1, 2, 3]` becomes `[3, 2, 1]`.

```
reverse_3([1, 2, 3]) -> [3, 2, 1]
reverse_3([5, 11, 9]) -> [9, 11, 5]
reverse_3([7, 0, 0]) -> [0, 0, 7]
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p112409) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def reverse_3(nums: List[int]) -> List[int]:
    pass


result = reverse_3([1, 2, 3])
print(result)
```

## Tests
```python
from main import reverse_3


def test_reverse_3_1():
    assert reverse_3([1, 2, 3]) == [3, 2, 1]


def test_reverse_3_2():
    assert reverse_3([5, 11, 9]) == [9, 11, 5]


def test_reverse_3_3():
    assert reverse_3([7, 0, 0]) == [0, 0, 7]


def test_reverse_3_4():
    assert reverse_3([2, 1, 2]) == [2, 1, 2]


def test_reverse_3_5():
    assert reverse_3([1, 2, 1]) == [1, 2, 1]


def test_reverse_3_6():
    assert reverse_3([2, 11, 3]) == [3, 11, 2]


def test_reverse_3_7():
    assert reverse_3([0, 6, 5]) == [5, 6, 0]


def test_reverse_3_8():
    assert reverse_3([7, 2, 3]) == [3, 2, 7]
```
