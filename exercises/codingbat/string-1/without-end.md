# without_end





Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.

```
without_end("Hello") â†’ "ell"
without_end("java") â†’ "av"
without_end("coding") â†’ "odin"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p130896) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def without_end(string: str) -> str:
    pass


result = without_end('Hello')
print(result)
```

## Tests
```python
from main import without_end


def test_without_end_1():
    assert without_end('Hello') == 'ell'


def test_without_end_2():
    assert without_end('java') == 'av'


def test_without_end_3():
    assert without_end('coding') == 'odin'


def test_without_end_4():
    assert without_end('code') == 'od'


def test_without_end_5():
    assert without_end('ab') == ''


def test_without_end_6():
    assert without_end('Chocolate!') == 'hocolate'


def test_without_end_7():
    assert without_end('kitten') == 'itte'


def test_without_end_8():
    assert without_end('woohoo') == 'ooho'
```
