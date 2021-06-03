# change_xy





Given a string, compute recursively (no loops) a new string where all the lowercase `'x'` chars have been changed to `'y'` chars.

```
change_xy("codex") -> "codey"
change_xy("xxhixx") -> "yyhiyy"
change_xy("xhixhix") -> "yhiyhiy"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p101372) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def change_xy(string: str) -> str:
    pass


result = change_xy('codex')
print(result)
```

## Tests
```python
from main import change_xy


def test_change_xy_1():
    assert change_xy('codex') == 'codey'


def test_change_xy_2():
    assert change_xy('xxhixx') == 'yyhiyy'


def test_change_xy_3():
    assert change_xy('xhixhix') == 'yhiyhiy'


def test_change_xy_4():
    assert change_xy('hiy') == 'hiy'


def test_change_xy_5():
    assert change_xy('h') == 'h'


def test_change_xy_6():
    assert change_xy('x') == 'y'


def test_change_xy_7():
    assert change_xy('') == ''


def test_change_xy_8():
    assert change_xy('xxx') == 'yyy'


def test_change_xy_9():
    assert change_xy('yyhxyi') == 'yyhyyi'


def test_change_xy_10():
    assert change_xy('hihi') == 'hihi'


def test_change_xy_11():
    assert change_xy('XxXx') == 'XyXy'
```
