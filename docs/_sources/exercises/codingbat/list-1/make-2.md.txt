# make_2





Given 2 int lists, a and b, return a new list length 2 containing, as much as will fit, the elements from a followed by the elements from b. The lists may be any length, including 0, but there will be 2 or more elements available between the 2 lists.

```
make_2([4, 5], [1, 2, 3]) -> [4, 5]
make_2([4], [1, 2, 3]) -> [4, 1]
make_2([], [1, 2]) -> [1, 2]
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p143461) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def make_2(a: List[int], b: List[int]) -> List[int]:
    pass


result = make_2([4, 5], [1, 2, 3])
print(result)
```

## Tests
```python
from main import make_2


def test_make_2_1():
    assert make_2([4, 5], [1, 2, 3]) == [4, 5]


def test_make_2_2():
    assert make_2([4], [1, 2, 3]) == [4, 1]


def test_make_2_3():
    assert make_2([], [1, 2]) == [1, 2]


def test_make_2_4():
    assert make_2([1, 2], []) == [1, 2]


def test_make_2_5():
    assert make_2([3], [1, 2, 3]) == [3, 1]


def test_make_2_6():
    assert make_2([3], [1]) == [3, 1]


def test_make_2_7():
    assert make_2([3, 1, 4], []) == [3, 1]


def test_make_2_8():
    assert make_2([1], [1]) == [1, 1]


def test_make_2_9():
    assert make_2([1, 2, 3], [7, 8]) == [1, 2]


def test_make_2_10():
    assert make_2([7, 8], [1, 2, 3]) == [7, 8]


def test_make_2_11():
    assert make_2([7], [1, 2, 3]) == [7, 1]


def test_make_2_12():
    assert make_2([5, 4], [2, 3, 7]) == [5, 4]
```
