# fix_23





Given an int list length 3, if there is a 2 in the list immediately followed by a 3, set the 3 element to 0. Return the changed list.

```
fix_23([1, 2, 3]) -> [1, 2, 0]
fix_23([2, 3, 5]) -> [2, 0, 5]
fix_23([1, 2, 1]) -> [1, 2, 1]
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p120347) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def fix_23(nums: List[int]) -> List[int]:
    pass


result = fix_23([1, 2, 3])
print(result)
```

## Tests
```python
from main import fix_23


def test_fix_23_1():
    assert fix_23([1, 2, 3]) == [1, 2, 0]


def test_fix_23_2():
    assert fix_23([2, 3, 5]) == [2, 0, 5]


def test_fix_23_3():
    assert fix_23([1, 2, 1]) == [1, 2, 1]


def test_fix_23_4():
    assert fix_23([3, 2, 1]) == [3, 2, 1]


def test_fix_23_5():
    assert fix_23([2, 2, 3]) == [2, 2, 0]


def test_fix_23_6():
    assert fix_23([2, 3, 3]) == [2, 0, 3]
```
