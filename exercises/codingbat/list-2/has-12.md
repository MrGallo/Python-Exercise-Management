# has_12





Given a list of ints, return true if there is a 1 in the list with a 2 somewhere later in the list.

```
has_12([1, 3, 2]) -> true
has_12([3, 1, 2]) -> true
has_12([3, 1, 4, 5, 2]) -> true
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p169260) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def has_12(nums: List[int]) -> bool:
    pass


result = has_12([1, 3, 2])
print(result)
```

## Tests
```python
from main import has_12


def test_has_12_1():
    assert has_12([1, 3, 2]) == True


def test_has_12_2():
    assert has_12([3, 1, 2]) == True


def test_has_12_3():
    assert has_12([3, 1, 4, 5, 2]) == True


def test_has_12_4():
    assert has_12([3, 1, 4, 5, 6]) == False


def test_has_12_5():
    assert has_12([3, 1, 4, 1, 6, 2]) == True


def test_has_12_6():
    assert has_12([2, 1, 4, 1, 6, 2]) == True


def test_has_12_7():
    assert has_12([2, 1, 4, 1, 6]) == False


def test_has_12_8():
    assert has_12([1]) == False


def test_has_12_9():
    assert has_12([2, 1, 3]) == False


def test_has_12_10():
    assert has_12([2, 1, 3, 2]) == True


def test_has_12_11():
    assert has_12([2]) == False


def test_has_12_12():
    assert has_12([3, 2]) == False


def test_has_12_13():
    assert has_12([3, 1, 3, 2]) == True


def test_has_12_14():
    assert has_12([3, 5, 9]) == False


def test_has_12_15():
    assert has_12([3, 5, 1]) == False


def test_has_12_16():
    assert has_12([3, 2, 1]) == False


def test_has_12_17():
    assert has_12([1, 2]) == True
```
