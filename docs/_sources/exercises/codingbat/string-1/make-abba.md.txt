# make_abba





Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".

```
make_abba("Hi", "Bye") â†’ "HiByeByeHi"
make_abba("Yo", "Alice") â†’ "YoAliceAliceYo"
make_abba("What", "Up") â†’ "WhatUpUpWhat"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p161056) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def make_abba(a: str, b: str) -> str:
    pass


result = make_abba('Hi', 'Bye')
print(result)
```

## Tests
```python
from main import make_abba


def test_make_abba_1():
    assert make_abba('Hi', 'Bye') == 'HiByeByeHi'


def test_make_abba_2():
    assert make_abba('Yo', 'Alice') == 'YoAliceAliceYo'


def test_make_abba_3():
    assert make_abba('What', 'Up') == 'WhatUpUpWhat'


def test_make_abba_4():
    assert make_abba('aaa', 'bbb') == 'aaabbbbbbaaa'


def test_make_abba_5():
    assert make_abba('x', 'y') == 'xyyx'


def test_make_abba_6():
    assert make_abba('x', '') == 'xx'


def test_make_abba_7():
    assert make_abba('', 'y') == 'yy'


def test_make_abba_8():
    assert make_abba('Bo', 'Ya') == 'BoYaYaBo'


def test_make_abba_9():
    assert make_abba('Ya', 'Ya') == 'YaYaYaYa'
```
