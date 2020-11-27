# icy_hot





Given two temperatures, return true if one is less than 0 and the other is greater than 100.

```
icy_hot(120, -1) → true
icy_hot(-1, 120) → true
icy_hot(2, 120) → false
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p192082) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def icy_hot(temp_1: int, temp_2: int) -> bool:
    pass


result = icy_hot(120, -1)
print(result)
```

## Tests
```python
from main import icy_hot


def test_icy_hot_1():
    assert icy_hot(120, -1) == True


def test_icy_hot_2():
    assert icy_hot(-1, 120) == True


def test_icy_hot_3():
    assert icy_hot(2, 120) == False


def test_icy_hot_4():
    assert icy_hot(-1, 100) == False


def test_icy_hot_5():
    assert icy_hot(-2, -2) == False


def test_icy_hot_6():
    assert icy_hot(120, 120) == False
```
