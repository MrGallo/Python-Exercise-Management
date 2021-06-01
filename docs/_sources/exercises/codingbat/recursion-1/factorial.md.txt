# factorial





Given n of 1 or more, return the factorial of n, which is n * (n-1) * (n-2) ... 1. Compute the result recursively (without loops).

```
factorial(1) -> 1
factorial(2) -> 2
factorial(3) -> 6
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p154669) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def factorial(n: int) -> int:
    pass


result = factorial(1)
print(result)
```

## Tests
```python
from main import factorial


def test_factorial_1():
    assert factorial(1) == 1


def test_factorial_2():
    assert factorial(2) == 2


def test_factorial_3():
    assert factorial(3) == 6


def test_factorial_4():
    assert factorial(4) == 24


def test_factorial_5():
    assert factorial(5) == 120


def test_factorial_6():
    assert factorial(6) == 720


def test_factorial_7():
    assert factorial(7) == 5040


def test_factorial_8():
    assert factorial(8) == 40320


def test_factorial_9():
    assert factorial(12) == 479001600
```
