# has_teen





We'll say that a number is "teen" if it is in the range 13..19 inclusive. Given 3 int values, return true if 1 or more of them are teen.

```
has_teen(13, 20, 10) â†’ true
has_teen(20, 19, 10) â†’ true
has_teen(20, 10, 13) â†’ true
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p178986) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def has_teen(a: int, b: int, c: int) -> bool:
    pass


result = has_teen(13, 20, 10)
print(result)
```

## Tests
```python
from main import has_teen


def test_has_teen_1():
    assert has_teen(13, 20, 10) == True


def test_has_teen_2():
    assert has_teen(20, 19, 10) == True


def test_has_teen_3():
    assert has_teen(20, 10, 13) == True


def test_has_teen_4():
    assert has_teen(1, 20, 12) == False


def test_has_teen_5():
    assert has_teen(19, 20, 12) == True


def test_has_teen_6():
    assert has_teen(12, 20, 19) == True


def test_has_teen_7():
    assert has_teen(12, 9, 20) == False


def test_has_teen_8():
    assert has_teen(12, 18, 20) == True


def test_has_teen_9():
    assert has_teen(14, 2, 20) == True


def test_has_teen_10():
    assert has_teen(4, 2, 20) == False


def test_has_teen_11():
    assert has_teen(11, 22, 22) == False
```
