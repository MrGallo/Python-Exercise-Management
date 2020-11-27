# first_two





Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "". Note that `len()` returns the length of a string.

```
first_two("Hello") → "He"
first_two("abcdefg") → "ab"
first_two("ab") → "ab"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p163411) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def first_two(string: str) -> str:
    pass


result = first_two('Hello')
print(result)
```

## Tests
```python
from main import first_two


def test_first_two_1():
    assert first_two('Hello') == 'He'


def test_first_two_2():
    assert first_two('abcdefg') == 'ab'


def test_first_two_3():
    assert first_two('ab') == 'ab'


def test_first_two_4():
    assert first_two('a') == 'a'


def test_first_two_5():
    assert first_two('') == ''


def test_first_two_6():
    assert first_two('Kitten') == 'Ki'


def test_first_two_7():
    assert first_two('hi') == 'hi'


def test_first_two_8():
    assert first_two('hiya') == 'hi'
```
