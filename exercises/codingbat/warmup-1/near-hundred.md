# near_hundred





Given an int n, return true if it is within 10 of 100 or 200. Note: Math.abs(num) computes the absolute value of a number.

```
near_hundred(93) → true
near_hundred(90) → true
near_hundred(89) → false
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p184004) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def near_hundred(n: int) -> bool:
    pass


result = near_hundred(93)
print(result)
```

## Tests
```python
from main import near_hundred


def test_near_hundred_1():
    assert near_hundred(93) == True


def test_near_hundred_2():
    assert near_hundred(90) == True


def test_near_hundred_3():
    assert near_hundred(89) == False


def test_near_hundred_4():
    assert near_hundred(110) == True


def test_near_hundred_5():
    assert near_hundred(111) == False


def test_near_hundred_6():
    assert near_hundred(121) == False


def test_near_hundred_7():
    assert near_hundred(-101) == False


def test_near_hundred_8():
    assert near_hundred(-209) == False


def test_near_hundred_9():
    assert near_hundred(190) == True


def test_near_hundred_10():
    assert near_hundred(209) == True


def test_near_hundred_11():
    assert near_hundred(0) == False


def test_near_hundred_12():
    assert near_hundred(5) == False


def test_near_hundred_13():
    assert near_hundred(-50) == False


def test_near_hundred_14():
    assert near_hundred(191) == True


def test_near_hundred_15():
    assert near_hundred(189) == False


def test_near_hundred_16():
    assert near_hundred(200) == True


def test_near_hundred_17():
    assert near_hundred(210) == True


def test_near_hundred_18():
    assert near_hundred(211) == False


def test_near_hundred_19():
    assert near_hundred(290) == False
```
