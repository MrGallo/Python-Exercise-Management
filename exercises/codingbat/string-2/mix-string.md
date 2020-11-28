# mix_string





Given two strings, <b>a</b> and <b>b</b>, create a bigger string made of the first char of a, the first char of b, the second char of a, the second char of b, and so on. Any leftover chars go at the end of the result.

```
mix_string("abc", "xyz") -> "axbycz"
mix_string("Hi", "There") -> "HTihere"
mix_string("xxxx", "There") -> "xTxhxexre"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p125185) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def mix_string(a: str, b: str) -> str:
    pass


result = mix_string('abc', 'xyz')
print(result)
```

## Tests
```python
from main import mix_string


def test_mix_string_1():
    assert mix_string('abc', 'xyz') == 'axbycz'


def test_mix_string_2():
    assert mix_string('Hi', 'There') == 'HTihere'


def test_mix_string_3():
    assert mix_string('xxxx', 'There') == 'xTxhxexre'


def test_mix_string_4():
    assert mix_string('xxx', 'X') == 'xXxx'


def test_mix_string_5():
    assert mix_string('2/', '27 around') == '22/7 around'


def test_mix_string_6():
    assert mix_string('', 'Hello') == 'Hello'


def test_mix_string_7():
    assert mix_string('Abc', '') == 'Abc'


def test_mix_string_8():
    assert mix_string('', '') == ''


def test_mix_string_9():
    assert mix_string('a', 'b') == 'ab'


def test_mix_string_10():
    assert mix_string('ax', 'b') == 'abx'


def test_mix_string_11():
    assert mix_string('a', 'bx') == 'abx'


def test_mix_string_12():
    assert mix_string('So', 'Long') == 'SLoong'


def test_mix_string_13():
    assert mix_string('Long', 'So') == 'LSoong'
```
