# int_max





Given three int values, a b c, return the largest.

```
int_max(1, 2, 3) â†’ 3
int_max(1, 3, 2) â†’ 3
int_max(3, 2, 1) â†’ 3
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p101887) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def int_max(a: int, b: int, c: int) -> int:
    pass


result = int_max(1, 2, 3)
print(result)
```

## Tests
```python
from main import int_max


def test_int_max_1():
    assert int_max(1, 2, 3) == 3


def test_int_max_2():
    assert int_max(1, 3, 2) == 3


def test_int_max_3():
    assert int_max(3, 2, 1) == 3


def test_int_max_4():
    assert int_max(9, 3, 3) == 9


def test_int_max_5():
    assert int_max(3, 9, 3) == 9


def test_int_max_6():
    assert int_max(3, 3, 9) == 9


def test_int_max_7():
    assert int_max(8, 2, 3) == 8


def test_int_max_8():
    assert int_max(-3, -1, -2) == -1


def test_int_max_9():
    assert int_max(6, 2, 5) == 6


def test_int_max_10():
    assert int_max(5, 6, 2) == 6


def test_int_max_11():
    assert int_max(5, 2, 6) == 6
```
