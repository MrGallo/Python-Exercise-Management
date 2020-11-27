# the_end





Given a string, return a string length 1 from its front, unless <b>front</b> is false, in which case return a string length 1 from its back. The string will be non-empty.

```
the_end("Hello", true) → "H"
the_end("Hello", false) → "o"
the_end("oh", true) → "o"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p162477) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def the_end(string: str, front: bool) -> str:
    pass


result = the_end('Hello', True)
print(result)
```

## Tests
```python
from main import the_end


def test_the_end_1():
    assert the_end('Hello', True) == 'H'


def test_the_end_2():
    assert the_end('Hello', False) == 'o'


def test_the_end_3():
    assert the_end('oh', True) == 'o'


def test_the_end_4():
    assert the_end('oh', False) == 'h'


def test_the_end_5():
    assert the_end('x', True) == 'x'


def test_the_end_6():
    assert the_end('x', False) == 'x'


def test_the_end_7():
    assert the_end('java', True) == 'j'


def test_the_end_8():
    assert the_end('chocolate', False) == 'e'


def test_the_end_9():
    assert the_end('1234', True) == '1'


def test_the_end_10():
    assert the_end('code', False) == 'e'
```
