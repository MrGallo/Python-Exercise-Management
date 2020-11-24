# last_chars
**Topic:** 



Given 2 strings, a and b, return a new string made of the first char of a and the last char of b, so "yo" and "java" yields "ya". If either string is length 0, use '@' for its missing char.

```
last_chars("last", "chars") → "ls"
last_chars("yo", "java") → "ya"
last_chars("hi", "") → "h@"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p138183) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def last_chars(a: str, b: str) -> str:
```

## Tests
```python
from main import last_chars


def test_last_chars_1():
    assert last_chars('last', 'chars') == 'ls'


def test_last_chars_2():
    assert last_chars('yo', 'java') == 'ya'


def test_last_chars_3():
    assert last_chars('hi', '') == 'h@'


def test_last_chars_4():
    assert last_chars('', 'hello') == '@o'


def test_last_chars_5():
    assert last_chars('', '') == '@@'


def test_last_chars_6():
    assert last_chars('kitten', 'hi') == 'ki'


def test_last_chars_7():
    assert last_chars('k', 'zip') == 'kp'


def test_last_chars_8():
    assert last_chars('kitten', '') == 'k@'


def test_last_chars_9():
    assert last_chars('kitten', 'zip') == 'kp'
```
