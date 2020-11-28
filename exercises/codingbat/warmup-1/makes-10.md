# makes_10





Given 2 ints, a and b, return true if one if them is 10 or if their sum is 10.

```
makes_10(9, 10) -> true
makes_10(9, 9) -> false
makes_10(1, 9) -> true
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p182873) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def makes_10(a: int, b: int) -> bool:
    pass


result = makes_10(9, 10)
print(result)
```

## Tests
```python
from main import makes_10


def test_makes_10_1():
    assert makes_10(9, 10) == True


def test_makes_10_2():
    assert makes_10(9, 9) == False


def test_makes_10_3():
    assert makes_10(1, 9) == True


def test_makes_10_4():
    assert makes_10(10, 1) == True


def test_makes_10_5():
    assert makes_10(10, 10) == True


def test_makes_10_6():
    assert makes_10(8, 2) == True


def test_makes_10_7():
    assert makes_10(8, 3) == False


def test_makes_10_8():
    assert makes_10(10, 42) == True


def test_makes_10_9():
    assert makes_10(12, -2) == True
```
