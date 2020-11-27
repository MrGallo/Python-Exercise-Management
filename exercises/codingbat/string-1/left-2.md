# left_2





Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.

```
left_2("Hello") â†’ "lloHe"
left_2("java") â†’ "vaja"
left_2("Hi") â†’ "Hi"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p197720) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def left_2(string: str) -> str:
    pass


result = left_2('Hello')
print(result)
```

## Tests
```python
from main import left_2


def test_left_2_1():
    assert left_2('Hello') == 'lloHe'


def test_left_2_2():
    assert left_2('java') == 'vaja'


def test_left_2_3():
    assert left_2('Hi') == 'Hi'


def test_left_2_4():
    assert left_2('code') == 'deco'


def test_left_2_5():
    assert left_2('cat') == 'tca'


def test_left_2_6():
    assert left_2('12345') == '34512'


def test_left_2_7():
    assert left_2('Chocolate') == 'ocolateCh'


def test_left_2_8():
    assert left_2('bricks') == 'icksbr'
```
