# front_back





Given a string, return a new string where the first and last chars have been exchanged.

```
front_back("code") → "eodc"
front_back("a") → "a"
front_back("ab") → "ba"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p123384) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def front_back(string: str) -> str:
    pass


result = front_back('code')
print(result)
```

## Tests
```python
from main import front_back


def test_front_back_1():
    assert front_back('code') == 'eodc'


def test_front_back_2():
    assert front_back('a') == 'a'


def test_front_back_3():
    assert front_back('ab') == 'ba'


def test_front_back_4():
    assert front_back('abc') == 'cba'


def test_front_back_5():
    assert front_back('') == ''


def test_front_back_6():
    assert front_back('Chocolate') == 'ehocolatC'


def test_front_back_7():
    assert front_back('aavJ') == 'Java'


def test_front_back_8():
    assert front_back('hello') == 'oellh'
```
