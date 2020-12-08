# zero_front





Return an list that contains the exact same numbers as the given list, but rearranged so that all the zeros are grouped at the start of the list. The order of the non-zero numbers does not matter. So {1, 0, 0, 1} becomes {0 ,0, 1, 1}. You may modify and return the given list or make a new list.

```
zero_front([1, 0, 0, 1]) -> [0, 0, 1, 1]
zero_front([0, 1, 1, 0, 1]) -> [0, 0, 1, 1, 1]
zero_front([1, 0]) -> [0, 1]
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p193753) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def zero_front(nums: List[int]) -> List[int]:
    pass


result = zero_front([1, 0, 0, 1])
print(result)
```

## Tests
```python
from main import zero_front


def test_zero_front_1():
    assert zero_front([1, 0, 0, 1]) == [0, 0, 1, 1]


def test_zero_front_2():
    assert zero_front([0, 1, 1, 0, 1]) == [0, 0, 1, 1, 1]


def test_zero_front_3():
    assert zero_front([1, 0]) == [0, 1]


def test_zero_front_4():
    assert zero_front([0, 1]) == [0, 1]


def test_zero_front_5():
    assert zero_front([1, 1, 1, 0]) == [0, 1, 1, 1]


def test_zero_front_6():
    assert zero_front([2, 2, 2, 2]) == [2, 2, 2, 2]


def test_zero_front_7():
    assert zero_front([0, 0, 1, 0]) == [0, 0, 0, 1]


def test_zero_front_8():
    assert zero_front([-1, 0, 0, -1, 0]) == [0, 0, 0, -1, -1]


def test_zero_front_9():
    assert zero_front([0, -3, 0, -3]) == [0, 0, -3, -3]


def test_zero_front_10():
    assert zero_front([]) == []


def test_zero_front_11():
    assert zero_front([9, 9, 0, 9, 0, 9]) == [0, 0, 9, 9, 9, 9]
```
