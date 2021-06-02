# sum_digits





Given a non-negative int `n`, return the sum of its digits recursively (no loops). Note that mod (`%`) by `10` yields the rightmost digit (`126 % 10` is `6`), while integer divide (`//`) by `10` removes the rightmost digit (`126 // 10` is `12`).

```
sum_digits(126) -> 9
sum_digits(49) -> 13
sum_digits(12) -> 3
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p163932) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def sum_digits(n: int) -> int:
    pass


result = sum_digits(126)
print(result)
```

## Tests
```python
from main import sum_digits


def test_sum_digits_1():
    assert sum_digits(126) == 9


def test_sum_digits_2():
    assert sum_digits(49) == 13


def test_sum_digits_3():
    assert sum_digits(12) == 3


def test_sum_digits_4():
    assert sum_digits(10) == 1


def test_sum_digits_5():
    assert sum_digits(1) == 1


def test_sum_digits_6():
    assert sum_digits(0) == 0


def test_sum_digits_7():
    assert sum_digits(730) == 10


def test_sum_digits_8():
    assert sum_digits(1111) == 4


def test_sum_digits_9():
    assert sum_digits(11111) == 5


def test_sum_digits_10():
    assert sum_digits(10110) == 3


def test_sum_digits_11():
    assert sum_digits(235) == 10
```
