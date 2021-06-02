# count_7





Given a non-negative int `n`, return the count of the occurrences of `7` as a digit, so for example `717` yields `2`. (no loops). Note that mod (`%`) by `10` yields the rightmost digit (`126 % 10` is `6`), while integer divide (`//`) by `10` removes the rightmost digit (`126 / 10` is `12`).

```
count_7(717) -> 2
count_7(7) -> 1
count_7(123) -> 0
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p101409) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def count_7(n: int) -> int:
    pass


result = count_7(717)
print(result)
```

## Tests
```python
from main import count_7


def test_count_7_1():
    assert count_7(717) == 2


def test_count_7_2():
    assert count_7(7) == 1


def test_count_7_3():
    assert count_7(123) == 0


def test_count_7_4():
    assert count_7(77) == 2


def test_count_7_5():
    assert count_7(7123) == 1


def test_count_7_6():
    assert count_7(771237) == 3


def test_count_7_7():
    assert count_7(771737) == 4


def test_count_7_8():
    assert count_7(47571) == 2


def test_count_7_9():
    assert count_7(777777) == 6


def test_count_7_10():
    assert count_7(70701277) == 4


def test_count_7_11():
    assert count_7(777576197) == 5


def test_count_7_12():
    assert count_7(99999) == 0


def test_count_7_13():
    assert count_7(99799) == 1
```
