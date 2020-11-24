# at_first
**Topic:** 



Given a string, return a string length 2 made of its first 2 chars. If the string length is less than 2, use '@' for the missing chars.

```
at_first("hello") → "he"
at_first("hi") → "hi"
at_first("h") → "h@"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p139076) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def at_first(str: str) -> str:
```

## Tests
```python
from main import at_first


def test_at_first_1():
    assert at_first('hello') == 'he'


def test_at_first_2():
    assert at_first('hi') == 'hi'


def test_at_first_3():
    assert at_first('h') == 'h@'


def test_at_first_4():
    assert at_first('') == '@@'


def test_at_first_5():
    assert at_first('kitten') == 'ki'


def test_at_first_6():
    assert at_first('java') == 'ja'


def test_at_first_7():
    assert at_first('j') == 'j@'
```
