# no_x





Given a string, compute recursively a new string where all the 'x' chars have been removed.

```
no_x("xaxb") -> "ab"
no_x("abc") -> "abc"
no_x("xx") -> ""
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p118230) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def no_x(string: str) -> str:
    pass


result = no_x('xaxb')
print(result)
```

## Tests
```python
from main import no_x


def test_no_x_1():
    assert no_x('xaxb') == 'ab'


def test_no_x_2():
    assert no_x('abc') == 'abc'


def test_no_x_3():
    assert no_x('xx') == ''


def test_no_x_4():
    assert no_x('') == ''


def test_no_x_5():
    assert no_x('axxbxx') == 'ab'


def test_no_x_6():
    assert no_x('Hellox') == 'Hello'
```
