# front_22





Given a string, take the first 2 chars and return the string with the 2 chars added at both the front and back, so "kitten" yields"kikittenki". If the string length is less than 2, use whatever chars are there.

```
front_22("kitten") → "kikittenki"
front_22("Ha") → "HaHaHa"
front_22("abc") → "ababcab"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p183592) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def front_22(string: str) -> str:
    pass


result = front_22('kitten')
print(result)
```

## Tests
```python
from main import front_22


def test_front_22_1():
    assert front_22('kitten') == 'kikittenki'


def test_front_22_2():
    assert front_22('Ha') == 'HaHaHa'


def test_front_22_3():
    assert front_22('abc') == 'ababcab'


def test_front_22_4():
    assert front_22('ab') == 'ababab'


def test_front_22_5():
    assert front_22('a') == 'aaa'


def test_front_22_6():
    assert front_22('') == ''


def test_front_22_7():
    assert front_22('Logic') == 'LoLogicLo'
```
