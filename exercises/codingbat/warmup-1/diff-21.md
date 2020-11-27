# diff_21





Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

```
diff_21(19) → 2
diff_21(10) → 11
diff_21(21) → 0
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p116624) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def diff_21(n: int) -> int:
    pass


result = diff_21(19)
print(result)
```

## Tests
```python
from main import diff_21


def test_diff_21_1():
    assert diff_21(19) == 2


def test_diff_21_2():
    assert diff_21(10) == 11


def test_diff_21_3():
    assert diff_21(21) == 0


def test_diff_21_4():
    assert diff_21(22) == 2


def test_diff_21_5():
    assert diff_21(25) == 8


def test_diff_21_6():
    assert diff_21(30) == 18


def test_diff_21_7():
    assert diff_21(0) == 21


def test_diff_21_8():
    assert diff_21(1) == 20


def test_diff_21_9():
    assert diff_21(2) == 19


def test_diff_21_10():
    assert diff_21(-1) == 22


def test_diff_21_11():
    assert diff_21(-2) == 23


def test_diff_21_12():
    assert diff_21(50) == 58
```
