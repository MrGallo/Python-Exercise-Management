# without_x_2
**Topic:** 



Given a string, if one or both of the first 2 chars is 'x', return the string without those 'x' chars, and otherwise return the string unchanged. This is a little harder than it looks.

```
without_x_2("xHi") → "Hi"
without_x_2("Hxi") → "Hi"
without_x_2("Hi") → "Hi"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p151359) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def without_x_2(str: str) -> str:
```

## Tests
```python
from main import without_x_2


def test_without_x_2_1():
    assert without_x_2('xHi') == 'Hi'


def test_without_x_2_2():
    assert without_x_2('Hxi') == 'Hi'


def test_without_x_2_3():
    assert without_x_2('Hi') == 'Hi'


def test_without_x_2_4():
    assert without_x_2('xxHi') == 'Hi'


def test_without_x_2_5():
    assert without_x_2('Hix') == 'Hix'


def test_without_x_2_6():
    assert without_x_2('xaxb') == 'axb'


def test_without_x_2_7():
    assert without_x_2('xx') == ''


def test_without_x_2_8():
    assert without_x_2('x') == ''


def test_without_x_2_9():
    assert without_x_2('') == ''


def test_without_x_2_10():
    assert without_x_2('Hello') == 'Hello'


def test_without_x_2_11():
    assert without_x_2('Hexllo') == 'Hexllo'


def test_without_x_2_12():
    assert without_x_2('xHxllo') == 'Hxllo'
```
