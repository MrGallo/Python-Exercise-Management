# count_8





Given a non-negative int n, compute recursively (no loops) the count of the occurrences of 8 as a digit, except that an 8 with another 8 immediately to its left counts double, so 8818 yields 4. Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

```
count_8(8) -> 1
count_8(818) -> 2
count_8(8818) -> 4
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p192383) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def count_8(n: int) -> int:
    pass


result = count_8(8)
print(result)
```

## Tests
```python
from main import count_8


def test_count_8_1():
    assert count_8(8) == 1


def test_count_8_2():
    assert count_8(818) == 2


def test_count_8_3():
    assert count_8(8818) == 4


def test_count_8_4():
    assert count_8(8088) == 4


def test_count_8_5():
    assert count_8(123) == 0


def test_count_8_6():
    assert count_8(81238) == 2


def test_count_8_7():
    assert count_8(88788) == 6


def test_count_8_8():
    assert count_8(8234) == 1


def test_count_8_9():
    assert count_8(2348) == 1


def test_count_8_10():
    assert count_8(23884) == 3


def test_count_8_11():
    assert count_8(0) == 0


def test_count_8_12():
    assert count_8(1818188) == 5


def test_count_8_13():
    assert count_8(8818181) == 5


def test_count_8_14():
    assert count_8(1080) == 1


def test_count_8_15():
    assert count_8(188) == 3


def test_count_8_16():
    assert count_8(88888) == 9


def test_count_8_17():
    assert count_8(9898) == 2


def test_count_8_18():
    assert count_8(78) == 1
```
