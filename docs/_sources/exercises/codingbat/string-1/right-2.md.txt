# right_2
**Topic:** 



Given a string, return a "rotated right 2" version where the last 2 chars are moved to the start. The string length will be at least 2.

```
right_2("Hello") → "loHel"
right_2("java") → "vaja"
right_2("Hi") → "Hi"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p130781) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def right_2(string: str) -> str:
```

## Tests
```python
from main import right_2


def test_right_2_1():
    assert right_2('Hello') == 'loHel'


def test_right_2_2():
    assert right_2('java') == 'vaja'


def test_right_2_3():
    assert right_2('Hi') == 'Hi'


def test_right_2_4():
    assert right_2('code') == 'deco'


def test_right_2_5():
    assert right_2('cat') == 'atc'


def test_right_2_6():
    assert right_2('12345') == '45123'
```
