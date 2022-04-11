# has_77





Given a list of ints, return true if the list contains two 7's next to each other, or there are two 7's separated by one element, such as with {7, 1, 7}.

```
has_77([1, 7, 7]) -> true
has_77([1, 7, 1, 7]) -> true
has_77([1, 7, 1, 1, 7]) -> false
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p168357) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def has_77(nums: List[int]) -> bool:
    pass


result = has_77([1, 7, 7])
print(result)
```

## Tests
```python
from main import has_77


def test_has_77_1():
    assert has_77([1, 7, 7]) == True


def test_has_77_2():
    assert has_77([1, 7, 1, 7]) == True


def test_has_77_3():
    assert has_77([1, 7, 1, 1, 7]) == False


def test_has_77_4():
    assert has_77([7, 7, 1, 1, 7]) == True


def test_has_77_5():
    assert has_77([2, 7, 2, 2, 7, 2]) == False


def test_has_77_6():
    assert has_77([2, 7, 2, 2, 7, 7]) == True


def test_has_77_7():
    assert has_77([7, 2, 7, 2, 2, 7]) == True


def test_has_77_8():
    assert has_77([7, 2, 6, 2, 2, 7]) == False


def test_has_77_9():
    assert has_77([7, 7, 7]) == True


def test_has_77_10():
    assert has_77([7, 1, 7]) == True


def test_has_77_11():
    assert has_77([7, 1, 1]) == False


def test_has_77_12():
    assert has_77([1, 2]) == False


def test_has_77_13():
    assert has_77([1, 7]) == False


def test_has_77_14():
    assert has_77([7]) == False
```
