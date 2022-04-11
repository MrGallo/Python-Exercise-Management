# rotate_left_3





Given a list of ints length 3, return a list with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.

```
rotate_left_3([1, 2, 3]) -> [2, 3, 1]
rotate_left_3([5, 11, 9]) -> [11, 9, 5]
rotate_left_3([7, 0, 0]) -> [0, 0, 7]
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p185139) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def rotate_left_3(nums: List[int]) -> List[int]:
    pass


result = rotate_left_3([1, 2, 3])
print(result)
```

## Tests
```python
from main import rotate_left_3


def test_rotate_left_3_1():
    assert rotate_left_3([1, 2, 3]) == [2, 3, 1]


def test_rotate_left_3_2():
    assert rotate_left_3([5, 11, 9]) == [11, 9, 5]


def test_rotate_left_3_3():
    assert rotate_left_3([7, 0, 0]) == [0, 0, 7]


def test_rotate_left_3_4():
    assert rotate_left_3([1, 2, 1]) == [2, 1, 1]


def test_rotate_left_3_5():
    assert rotate_left_3([0, 0, 1]) == [0, 1, 0]
```
