# end_up





Given a string, return a new string where the last 3 chars are now in upper case. If the string has less than 3 chars, uppercase whatever is there. Note that str.toUpperCase() returns the uppercase version of a string.

```
end_up("Hello") → "HeLLO"
end_up("hi there") → "hi thERE"
end_up("hi") → "HI"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p125268) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def end_up(string: str) -> str:
    pass


result = end_up('Hello')
print(result)
```

## Tests
```python
from main import end_up


def test_end_up_1():
    assert end_up('Hello') == 'HeLLO'


def test_end_up_2():
    assert end_up('hi there') == 'hi thERE'


def test_end_up_3():
    assert end_up('hi') == 'HI'


def test_end_up_4():
    assert end_up('woo hoo') == 'woo HOO'


def test_end_up_5():
    assert end_up('xyz12') == 'xyZ12'


def test_end_up_6():
    assert end_up('x') == 'X'


def test_end_up_7():
    assert end_up('') == ''
```
