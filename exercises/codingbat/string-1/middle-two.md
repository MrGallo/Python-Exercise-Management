# middle_two





Given a string of even length, return a string made of the middle two chars, so the string "string" yields "ri". The string length will be at least 2.

```
middle_two("string") → "ri"
middle_two("code") → "od"
middle_two("Practice") → "ct"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p137729) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def middle_two(string: str) -> str:
    pass


result = middle_two('string')
print(result)
```

## Tests
```python
from main import middle_two


def test_middle_two_1():
    assert middle_two('string') == 'ri'


def test_middle_two_2():
    assert middle_two('code') == 'od'


def test_middle_two_3():
    assert middle_two('Practice') == 'ct'


def test_middle_two_4():
    assert middle_two('ab') == 'ab'


def test_middle_two_5():
    assert middle_two('0123456789') == '45'
```
