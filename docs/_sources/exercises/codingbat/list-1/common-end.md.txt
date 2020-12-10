# common_end



**Requirements:**
```eval_rst
- :ref:`fundamentals:if, elif, else`
- :ref:`fundamentals:accessing list elements`

```


Given 2 lists of ints, a and b, return true if they have the same first element or they have the same last element. Both lists will be length 1 or more.

```
common_end([1, 2, 3], [7, 3]) -> true
common_end([1, 2, 3], [7, 3, 2]) -> false
common_end([1, 2, 3], [1, 3]) -> true
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p191991) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def common_end(a: List[int], b: List[int]) -> bool:
    pass


result = common_end([1, 2, 3], [7, 3])
print(result)
```

## Tests
```python
from main import common_end


def test_common_end_1():
    assert common_end([1, 2, 3], [7, 3]) == True


def test_common_end_2():
    assert common_end([1, 2, 3], [7, 3, 2]) == False


def test_common_end_3():
    assert common_end([1, 2, 3], [1, 3]) == True


def test_common_end_4():
    assert common_end([1, 2, 3], [1]) == True


def test_common_end_5():
    assert common_end([1, 2, 3], [2]) == False
```
