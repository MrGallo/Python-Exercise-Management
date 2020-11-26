# start_hi




Given a string, return true if the string starts with "hi" and false otherwise.

```
start_hi("hi there") → true
start_hi("hi") → true
start_hi("hello hi") → false
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p191022) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def start_hi(string: str) -> bool:
    pass


result = start_hi('hi there')
print(result)
```

## Tests
```python
from main import start_hi


def test_start_hi_1():
    assert start_hi('hi there') == True


def test_start_hi_2():
    assert start_hi('hi') == True


def test_start_hi_3():
    assert start_hi('hello hi') == False


def test_start_hi_4():
    assert start_hi('he') == False


def test_start_hi_5():
    assert start_hi('h') == False


def test_start_hi_6():
    assert start_hi('') == False


def test_start_hi_7():
    assert start_hi('ho hi') == False


def test_start_hi_8():
    assert start_hi('hi ho') == True
```
