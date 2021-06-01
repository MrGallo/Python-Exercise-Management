# fibonacci





The fibonacci sequence is a famous bit of mathematics, and it happens to have a recursive definition. The first two values in the sequence are 0 and 1 (essentially 2 base cases). Each subsequent value is the sum of the previous two values, so the whole sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21 and so on. Define a recursive fibonacci(n) method that returns the nth fibonacci number, with n=0 representing the start of the sequence.

```
fibonacci(0) -> 0
fibonacci(1) -> 1
fibonacci(2) -> 1
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p120015) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def fibonacci(n: int) -> int:
    pass


result = fibonacci(0)
print(result)
```

## Tests
```python
from main import fibonacci


def test_fibonacci_1():
    assert fibonacci(0) == 0


def test_fibonacci_2():
    assert fibonacci(1) == 1


def test_fibonacci_3():
    assert fibonacci(2) == 1


def test_fibonacci_4():
    assert fibonacci(3) == 2


def test_fibonacci_5():
    assert fibonacci(4) == 3


def test_fibonacci_6():
    assert fibonacci(5) == 5


def test_fibonacci_7():
    assert fibonacci(6) == 8


def test_fibonacci_8():
    assert fibonacci(7) == 13
```
