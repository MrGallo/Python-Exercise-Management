# mid_three





Given a list of ints of odd length, return a new list length 3 containing the elements from the middle of the list. The list length will be at least 3.

```
mid_three([1, 2, 3, 4, 5]) -> [2, 3, 4]
mid_three([8, 6, 7, 5, 3, 0, 9]) -> [7, 5, 3]
mid_three([1, 2, 3]) -> [1, 2, 3]
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p155713) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def mid_three(nums: List[int]) -> List[int]:
    pass


result = mid_three([1, 2, 3, 4, 5])
print(result)
```

## Tests
```python
from main import mid_three


def test_mid_three_1():
    assert mid_three([1, 2, 3, 4, 5]) == [2, 3, 4]


def test_mid_three_2():
    assert mid_three([8, 6, 7, 5, 3, 0, 9]) == [7, 5, 3]


def test_mid_three_3():
    assert mid_three([1, 2, 3]) == [1, 2, 3]
```
