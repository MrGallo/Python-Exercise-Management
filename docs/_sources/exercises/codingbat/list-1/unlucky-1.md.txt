# unlucky_1





We'll say that a 1 immediately followed by a 3 in an list is an "unlucky" 1. Return true if the given list contains an unlucky 1 in the first 2 or last 2 positions in the list.

```
unlucky_1([1, 3, 4, 5]) -> true
unlucky_1([2, 1, 3, 4, 5]) -> true
unlucky_1([1, 1, 1]) -> false
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p197308) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def unlucky_1(nums: List[int]) -> bool:
    pass


result = unlucky_1([1, 3, 4, 5])
print(result)
```

## Tests
```python
from main import unlucky_1


def test_unlucky_1_1():
    assert unlucky_1([1, 3, 4, 5]) == True


def test_unlucky_1_2():
    assert unlucky_1([2, 1, 3, 4, 5]) == True


def test_unlucky_1_3():
    assert unlucky_1([1, 1, 1]) == False


def test_unlucky_1_4():
    assert unlucky_1([1, 3, 1]) == True


def test_unlucky_1_5():
    assert unlucky_1([1, 1, 3]) == True


def test_unlucky_1_6():
    assert unlucky_1([1, 2, 3]) == False


def test_unlucky_1_7():
    assert unlucky_1([3, 3, 3]) == False


def test_unlucky_1_8():
    assert unlucky_1([1, 3]) == True


def test_unlucky_1_9():
    assert unlucky_1([1, 4]) == False


def test_unlucky_1_10():
    assert unlucky_1([1]) == False


def test_unlucky_1_11():
    assert unlucky_1([]) == False


def test_unlucky_1_12():
    assert unlucky_1([1, 1, 1, 3, 1]) == False


def test_unlucky_1_13():
    assert unlucky_1([1, 1, 3, 1, 1]) == True


def test_unlucky_1_14():
    assert unlucky_1([1, 1, 1, 1, 3]) == True


def test_unlucky_1_15():
    assert unlucky_1([1, 4, 1, 5]) == False


def test_unlucky_1_16():
    assert unlucky_1([1, 1, 2, 3]) == False


def test_unlucky_1_17():
    assert unlucky_1([2, 3, 2, 1]) == False


def test_unlucky_1_18():
    assert unlucky_1([2, 3, 1, 3]) == True


def test_unlucky_1_19():
    assert unlucky_1([1, 2, 3, 4, 1, 3]) == True
```
