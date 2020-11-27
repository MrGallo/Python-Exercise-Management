# back_around





Given a string, take the last char and return a new string with the last char added at the front and back, so "cat" yields "tcatt". The original string will be length 1 or more.

```
back_around("cat") → "tcatt"
back_around("Hello") → "oHelloo"
back_around("a") → "aaa"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p161642) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def back_around(string: str) -> str:
    pass


result = back_around('cat')
print(result)
```

## Tests
```python
from main import back_around


def test_back_around_1():
    assert back_around('cat') == 'tcatt'


def test_back_around_2():
    assert back_around('Hello') == 'oHelloo'


def test_back_around_3():
    assert back_around('a') == 'aaa'


def test_back_around_4():
    assert back_around('abc') == 'cabcc'


def test_back_around_5():
    assert back_around('read') == 'dreadd'


def test_back_around_6():
    assert back_around('boo') == 'obooo'
```
