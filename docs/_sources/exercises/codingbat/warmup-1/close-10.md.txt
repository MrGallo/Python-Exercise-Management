# close_10





Given 2 int values, return whichever value is nearest to the value 10, or return 0 in the event of a tie. Note that Math.abs(n) returns the absolute value of a number.

```
close_10(8, 13) â†’ 8
close_10(13, 8) â†’ 8
close_10(13, 7) â†’ 0
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p172021) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def close_10(a: int, b: int) -> int:
    pass


result = close_10(8, 13)
print(result)
```

## Tests
```python
from main import close_10


def test_close_10_1():
    assert close_10(8, 13) == 8


def test_close_10_2():
    assert close_10(13, 8) == 8


def test_close_10_3():
    assert close_10(13, 7) == 0


def test_close_10_4():
    assert close_10(7, 13) == 0


def test_close_10_5():
    assert close_10(9, 13) == 9


def test_close_10_6():
    assert close_10(13, 8) == 8


def test_close_10_7():
    assert close_10(10, 12) == 10


def test_close_10_8():
    assert close_10(11, 10) == 10


def test_close_10_9():
    assert close_10(5, 21) == 5


def test_close_10_10():
    assert close_10(0, 20) == 0


def test_close_10_11():
    assert close_10(10, 10) == 0
```
