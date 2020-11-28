# has_bad





Given a string, return true if "bad" appears starting at index 0 or 1 in the string, such as with "badxxx" or "xbadxx" but not "xxbadxx". The string may be any length, including 0. Note: use .equals() to compare 2 strings.

```
has_bad("badxx") -> true
has_bad("xbadxx") -> true
has_bad("xxbadxx") -> false
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p139075) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def has_bad(string: str) -> bool:
    pass


result = has_bad('badxx')
print(result)
```

## Tests
```python
from main import has_bad


def test_has_bad_1():
    assert has_bad('badxx') == True


def test_has_bad_2():
    assert has_bad('xbadxx') == True


def test_has_bad_3():
    assert has_bad('xxbadxx') == False


def test_has_bad_4():
    assert has_bad('code') == False


def test_has_bad_5():
    assert has_bad('bad') == True


def test_has_bad_6():
    assert has_bad('ba') == False


def test_has_bad_7():
    assert has_bad('xba') == False


def test_has_bad_8():
    assert has_bad('xbad') == True


def test_has_bad_9():
    assert has_bad('') == False


def test_has_bad_10():
    assert has_bad('badyy') == True
```
