# without_2
**Topic:** 



Given a string, if a length 2 substring appears at both its beginning and end, return a string without the substring at the beginning, so "HelloHe" yields "lloHe". The substring may overlap with itself, so "Hi" yields "". Otherwise, return the original string unchanged.

<code>
without_2("HelloHe") → "lloHe"
without_2("HelloHi") → "HelloHi"
without_2("Hi") → ""
</code>

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p142247) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def without_2(str: str) -> str:
```

## Tests
```python
from main import without_2


def test_without_2_1():
    assert without_2('HelloHe') == 'lloHe'


def test_without_2_2():
    assert without_2('HelloHi') == 'HelloHi'


def test_without_2_3():
    assert without_2('Hi') == ''


def test_without_2_4():
    assert without_2('Chocolate') == 'Chocolate'


def test_without_2_5():
    assert without_2('xxx') == 'x'


def test_without_2_6():
    assert without_2('xx') == ''


def test_without_2_7():
    assert without_2('x') == 'x'


def test_without_2_8():
    assert without_2('') == ''


def test_without_2_9():
    assert without_2('Fruits') == 'Fruits'
```
