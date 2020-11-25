# without_x




Given a string, if the first or last chars are 'x', return the string without those 'x' chars, and otherwise return the string unchanged.

```
without_x("xHix") → "Hi"
without_x("xHi") → "Hi"
without_x("Hxix") → "Hxi"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p151940) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def without_x(string: str) -> str:
    pass


result = without_x('xHix')
print(result)
```

## Tests
```python
from main import without_x


def test_without_x_1():
    assert without_x('xHix') == 'Hi'


def test_without_x_2():
    assert without_x('xHi') == 'Hi'


def test_without_x_3():
    assert without_x('Hxix') == 'Hxi'


def test_without_x_4():
    assert without_x('Hi') == 'Hi'


def test_without_x_5():
    assert without_x('xxHi') == 'xHi'


def test_without_x_6():
    assert without_x('Hix') == 'Hi'


def test_without_x_7():
    assert without_x('xaxbx') == 'axb'


def test_without_x_8():
    assert without_x('xx') == ''


def test_without_x_9():
    assert without_x('x') == ''


def test_without_x_10():
    assert without_x('') == ''


def test_without_x_11():
    assert without_x('Hello') == 'Hello'


def test_without_x_12():
    assert without_x('Hexllo') == 'Hexllo'
```
