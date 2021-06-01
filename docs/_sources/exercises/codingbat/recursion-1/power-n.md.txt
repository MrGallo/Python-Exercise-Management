# power_n





Given <b>base</b> and <b>n</b> that are both 1 or more, compute recursively (no loops) the value of base to the n power, so power_n(3, 2) is 9 (3 squared).

```
power_n(3, 1) -> 3
power_n(3, 2) -> 9
power_n(3, 3) -> 27
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p158888) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def power_n(base: int, n: int) -> int:
    pass


result = power_n(3, 1)
print(result)
```

## Tests
```python
from main import power_n


def test_power_n_1():
    assert power_n(3, 1) == 3


def test_power_n_2():
    assert power_n(3, 2) == 9


def test_power_n_3():
    assert power_n(3, 3) == 27


def test_power_n_4():
    assert power_n(2, 1) == 2


def test_power_n_5():
    assert power_n(2, 2) == 4


def test_power_n_6():
    assert power_n(2, 3) == 8


def test_power_n_7():
    assert power_n(2, 4) == 16


def test_power_n_8():
    assert power_n(2, 5) == 32


def test_power_n_9():
    assert power_n(10, 1) == 10


def test_power_n_10():
    assert power_n(10, 2) == 100


def test_power_n_11():
    assert power_n(10, 3) == 1000
```
