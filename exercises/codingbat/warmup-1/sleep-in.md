# sleep_in




The parameter weekday is true if it is a weekday, and the parameter vacation is true if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return true if we sleep in.

```
sleep_in(false, false) → true
sleep_in(true, false) → false
sleep_in(false, true) → true
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p187868) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def sleep_in(weekday: bool, vacation: bool) -> bool:
    pass


result = sleep_in(False, False)
print(result)
```

## Tests
```python
from main import sleep_in


def test_sleep_in_1():
    assert sleep_in(False, False) == True


def test_sleep_in_2():
    assert sleep_in(True, False) == False


def test_sleep_in_3():
    assert sleep_in(False, True) == True


def test_sleep_in_4():
    assert sleep_in(True, True) == True
```
