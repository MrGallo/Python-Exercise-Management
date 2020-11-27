# front_3





Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.

```
front_3("Java") → "JavJavJav"
front_3("Chocolate") → "ChoChoCho"
front_3("abc") → "abcabcabc"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p136351) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def front_3(string: str) -> str:
    pass


result = front_3('Java')
print(result)
```

## Tests
```python
from main import front_3


def test_front_3_1():
    assert front_3('Java') == 'JavJavJav'


def test_front_3_2():
    assert front_3('Chocolate') == 'ChoChoCho'


def test_front_3_3():
    assert front_3('abc') == 'abcabcabc'


def test_front_3_4():
    assert front_3('abcXYZ') == 'abcabcabc'


def test_front_3_5():
    assert front_3('ab') == 'ababab'


def test_front_3_6():
    assert front_3('a') == 'aaa'


def test_front_3_7():
    assert front_3('') == ''
```
