# triple_up





Return true if the list contains, somewhere, three increasing adjacent numbers like .... 4, 5, 6, ... or 23, 24, 25.

```
triple_up([1, 4, 5, 6, 2]) -> true
triple_up([1, 2, 3]) -> true
triple_up([1, 2, 4]) -> false
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p137874) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def triple_up(nums: List[int]) -> bool:
    pass


result = triple_up([1, 4, 5, 6, 2])
print(result)
```

## Tests
```python
from main import triple_up


def test_triple_up_1():
    assert triple_up([1, 4, 5, 6, 2]) == True


def test_triple_up_2():
    assert triple_up([1, 2, 3]) == True


def test_triple_up_3():
    assert triple_up([1, 2, 4]) == False


def test_triple_up_4():
    assert triple_up([1, 2, 4, 5, 7, 6, 5, 6, 7, 6]) == True


def test_triple_up_5():
    assert triple_up([1, 2, 4, 5, 7, 6, 5, 7, 7, 6]) == False


def test_triple_up_6():
    assert triple_up([1, 2]) == False


def test_triple_up_7():
    assert triple_up([1]) == False


def test_triple_up_8():
    assert triple_up([]) == False


def test_triple_up_9():
    assert triple_up([10, 9, 8, -100, -99, -98, 100]) == True


def test_triple_up_10():
    assert triple_up([10, 9, 8, -100, -99, 99, 100]) == False


def test_triple_up_11():
    assert triple_up([-100, -99, -99, 100, 101, 102]) == True


def test_triple_up_12():
    assert triple_up([2, 3, 5, 6, 8, 9, 2, 3]) == False
```
