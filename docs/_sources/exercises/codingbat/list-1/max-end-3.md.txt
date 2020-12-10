# max_end_3



**Requirements:**
```eval_rst
- :ref:`fundamentals:if, else`
- :ref:`fundamentals:creating a list`
- :ref:`fundamentals:accessing list elements`

```


Given an list of ints length 3, figure out which is larger, the first or last element in the list, and set all the other elements to be that value. Return the changed list.

```
max_end_3([1, 2, 3]) -> [3, 3, 3]
max_end_3([11, 5, 9]) -> [11, 11, 11]
max_end_3([2, 11, 3]) -> [3, 3, 3]
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p146256) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def max_end_3(nums: List[int]) -> List[int]:
    pass


result = max_end_3([1, 2, 3])
print(result)
```

## Tests
```python
from main import max_end_3


def test_max_end_3_1():
    assert max_end_3([1, 2, 3]) == [3, 3, 3]


def test_max_end_3_2():
    assert max_end_3([11, 5, 9]) == [11, 11, 11]


def test_max_end_3_3():
    assert max_end_3([2, 11, 3]) == [3, 3, 3]


def test_max_end_3_4():
    assert max_end_3([11, 3, 3]) == [11, 11, 11]


def test_max_end_3_5():
    assert max_end_3([3, 11, 11]) == [11, 11, 11]


def test_max_end_3_6():
    assert max_end_3([2, 2, 2]) == [2, 2, 2]


def test_max_end_3_7():
    assert max_end_3([2, 11, 2]) == [2, 2, 2]


def test_max_end_3_8():
    assert max_end_3([0, 0, 1]) == [1, 1, 1]
```
