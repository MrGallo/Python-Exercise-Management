# sum_double





Given two int values, return their sum. Unless the two values are the same, then return double their sum.

```
sum_double(1, 2) -> 3
sum_double(3, 2) -> 5
sum_double(2, 2) -> 8
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p154485) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def sum_double(a: int, b: int) -> int:
    pass


result = sum_double(1, 2)
print(result)
```

## Tests
```python
from main import sum_double


def test_sum_double_1():
    assert sum_double(1, 2) == 3


def test_sum_double_2():
    assert sum_double(3, 2) == 5


def test_sum_double_3():
    assert sum_double(2, 2) == 8


def test_sum_double_4():
    assert sum_double(-1, 0) == -1


def test_sum_double_5():
    assert sum_double(3, 3) == 12


def test_sum_double_6():
    assert sum_double(0, 0) == 0


def test_sum_double_7():
    assert sum_double(0, 1) == 1


def test_sum_double_8():
    assert sum_double(3, 4) == 7
```
