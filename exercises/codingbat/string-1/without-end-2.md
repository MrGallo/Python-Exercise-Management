# without_end_2
**Topic:** 



Given a string, return a version without both the first and last char of the string. The string may be any length, including 0.

```
without_end_2("Hello") → "ell"
without_end_2("abc") → "b"
without_end_2("ab") → ""
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p174254) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def without_end_2(string: str) -> str:
```

## Tests
```python
from main import without_end_2


def test_without_end_2_1():
    assert without_end_2('Hello') == 'ell'


def test_without_end_2_2():
    assert without_end_2('abc') == 'b'


def test_without_end_2_3():
    assert without_end_2('ab') == ''


def test_without_end_2_4():
    assert without_end_2('a') == ''


def test_without_end_2_5():
    assert without_end_2('') == ''


def test_without_end_2_6():
    assert without_end_2('coldy') == 'old'


def test_without_end_2_7():
    assert without_end_2('java code') == 'ava cod'
```
