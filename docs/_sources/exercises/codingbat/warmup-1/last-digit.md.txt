# last_digit





Given two non-negative int values, return true if they have the same last digit, such as with 27 and 57. Note that the % "mod" operator computes remainders, so 17 % 10 is 7.

```
last_digit(7, 17) -> true
last_digit(6, 17) -> false
last_digit(3, 113) -> true
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p125339) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def last_digit(a: int, b: int) -> bool:
    pass


result = last_digit(7, 17)
print(result)
```

## Tests
```python
from main import last_digit


def test_last_digit_1():
    assert last_digit(7, 17) == True


def test_last_digit_2():
    assert last_digit(6, 17) == False


def test_last_digit_3():
    assert last_digit(3, 113) == True


def test_last_digit_4():
    assert last_digit(114, 113) == False


def test_last_digit_5():
    assert last_digit(114, 4) == True


def test_last_digit_6():
    assert last_digit(10, 0) == True


def test_last_digit_7():
    assert last_digit(11, 0) == False
```
