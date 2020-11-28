# parrot_trouble





We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return true if we are in trouble.

```
parrot_trouble(true, 6) -> true
parrot_trouble(true, 7) -> false
parrot_trouble(false, 6) -> false
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p140449) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def parrot_trouble(talking: bool, hour: int) -> bool:
    pass


result = parrot_trouble(True, 6)
print(result)
```

## Tests
```python
from main import parrot_trouble


def test_parrot_trouble_1():
    assert parrot_trouble(True, 6) == True


def test_parrot_trouble_2():
    assert parrot_trouble(True, 7) == False


def test_parrot_trouble_3():
    assert parrot_trouble(False, 6) == False


def test_parrot_trouble_4():
    assert parrot_trouble(True, 21) == True


def test_parrot_trouble_5():
    assert parrot_trouble(False, 21) == False


def test_parrot_trouble_6():
    assert parrot_trouble(False, 20) == False


def test_parrot_trouble_7():
    assert parrot_trouble(True, 23) == True


def test_parrot_trouble_8():
    assert parrot_trouble(False, 23) == False


def test_parrot_trouble_9():
    assert parrot_trouble(True, 20) == False


def test_parrot_trouble_10():
    assert parrot_trouble(False, 12) == False
```
