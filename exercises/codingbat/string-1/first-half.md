# first_half





Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

```
first_half("WooHoo") → "Woo"
first_half("HelloThere") → "Hello"
first_half("abcdef") → "abc"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p172267) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def first_half(string: str) -> str:
    pass


result = first_half('WooHoo')
print(result)
```

## Tests
```python
from main import first_half


def test_first_half_1():
    assert first_half('WooHoo') == 'Woo'


def test_first_half_2():
    assert first_half('HelloThere') == 'Hello'


def test_first_half_3():
    assert first_half('abcdef') == 'abc'


def test_first_half_4():
    assert first_half('ab') == 'a'


def test_first_half_5():
    assert first_half('') == ''


def test_first_half_6():
    assert first_half('0123456789') == '01234'


def test_first_half_7():
    assert first_half('kitten') == 'kit'
```
