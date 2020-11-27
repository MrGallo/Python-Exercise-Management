# lone_teen





We'll say that a number is "teen" if it is in the range 13..19 inclusive. Given 2 int values, return true if one or the other is teen, but not both.

```
lone_teen(13, 99) → true
lone_teen(21, 19) → true
lone_teen(13, 13) → false
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p165701) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def lone_teen(a: int, b: int) -> bool:
    pass


result = lone_teen(13, 99)
print(result)
```

## Tests
```python
from main import lone_teen


def test_lone_teen_1():
    assert lone_teen(13, 99) == True


def test_lone_teen_2():
    assert lone_teen(21, 19) == True


def test_lone_teen_3():
    assert lone_teen(13, 13) == False


def test_lone_teen_4():
    assert lone_teen(14, 20) == True


def test_lone_teen_5():
    assert lone_teen(20, 15) == True


def test_lone_teen_6():
    assert lone_teen(16, 17) == False


def test_lone_teen_7():
    assert lone_teen(16, 9) == True


def test_lone_teen_8():
    assert lone_teen(16, 18) == False


def test_lone_teen_9():
    assert lone_teen(13, 19) == False


def test_lone_teen_10():
    assert lone_teen(13, 20) == True


def test_lone_teen_11():
    assert lone_teen(6, 18) == True


def test_lone_teen_12():
    assert lone_teen(99, 13) == True


def test_lone_teen_13():
    assert lone_teen(99, 99) == False
```
