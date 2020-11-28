# non_start





Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.

```
non_start("Hello", "There") -> "ellohere"
non_start("java", "code") -> "avaode"
non_start("shotl", "java") -> "hotlava"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p143825) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def non_start(a: str, b: str) -> str:
    pass


result = non_start('Hello', 'There')
print(result)
```

## Tests
```python
from main import non_start


def test_non_start_1():
    assert non_start('Hello', 'There') == 'ellohere'


def test_non_start_2():
    assert non_start('java', 'code') == 'avaode'


def test_non_start_3():
    assert non_start('shotl', 'java') == 'hotlava'


def test_non_start_4():
    assert non_start('ab', 'xy') == 'by'


def test_non_start_5():
    assert non_start('ab', 'x') == 'b'


def test_non_start_6():
    assert non_start('x', 'ac') == 'c'


def test_non_start_7():
    assert non_start('a', 'x') == ''


def test_non_start_8():
    assert non_start('kit', 'kat') == 'itat'


def test_non_start_9():
    assert non_start('mart', 'dart') == 'artart'
```
