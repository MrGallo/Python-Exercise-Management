# pos_neg





Given 2 int values, return true if one is negative and one is positive. Except if the parameter "negative" is true, then return true only if both are negative.

```
pos_neg(1, -1, false) → true
pos_neg(-1, 1, false) → true
pos_neg(-4, -5, true) → true
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p159227) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def pos_neg(a: int, b: int, negative: bool) -> bool:
    pass


result = pos_neg(1, -1, False)
print(result)
```

## Tests
```python
from main import pos_neg


def test_pos_neg_1():
    assert pos_neg(1, -1, False) == True


def test_pos_neg_2():
    assert pos_neg(-1, 1, False) == True


def test_pos_neg_3():
    assert pos_neg(-4, -5, True) == True


def test_pos_neg_4():
    assert pos_neg(-4, -5, False) == False


def test_pos_neg_5():
    assert pos_neg(-4, 5, False) == True


def test_pos_neg_6():
    assert pos_neg(-4, 5, True) == False


def test_pos_neg_7():
    assert pos_neg(1, 1, False) == False


def test_pos_neg_8():
    assert pos_neg(-1, -1, False) == False


def test_pos_neg_9():
    assert pos_neg(1, -1, True) == False


def test_pos_neg_10():
    assert pos_neg(-1, 1, True) == False


def test_pos_neg_11():
    assert pos_neg(1, 1, True) == False


def test_pos_neg_12():
    assert pos_neg(-1, -1, True) == True


def test_pos_neg_13():
    assert pos_neg(5, -5, False) == True


def test_pos_neg_14():
    assert pos_neg(-6, 6, False) == True


def test_pos_neg_15():
    assert pos_neg(-5, -6, False) == False


def test_pos_neg_16():
    assert pos_neg(-2, -1, False) == False


def test_pos_neg_17():
    assert pos_neg(1, 2, False) == False


def test_pos_neg_18():
    assert pos_neg(-5, 6, True) == False


def test_pos_neg_19():
    assert pos_neg(-5, -5, True) == True
```
