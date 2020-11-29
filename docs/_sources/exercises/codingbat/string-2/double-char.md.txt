# double_char



**Requirements:**
```eval_rst
- :ref:`fundamentals:string building and filtering`
- :ref:`fundamentals:returning a value`

```


Given a string, return a string where for every char in the original, there are two chars.

```
double_char("The") -> "TThhee"
double_char("AAbb") -> "AAAAbbbb"
double_char("Hi-There") -> "HHii--TThheerree"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p165312) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def double_char(string: str) -> str:
    pass


result = double_char('The')
print(result)
```

## Tests
```python
from main import double_char


def test_double_char_1():
    assert double_char('The') == 'TThhee'


def test_double_char_2():
    assert double_char('AAbb') == 'AAAAbbbb'


def test_double_char_3():
    assert double_char('Hi-There') == 'HHii--TThheerree'


def test_double_char_4():
    assert double_char('Word!') == 'WWoorrdd!!'


def test_double_char_5():
    assert double_char('!!') == '!!!!'


def test_double_char_6():
    assert double_char('') == ''


def test_double_char_7():
    assert double_char('a') == 'aa'


def test_double_char_8():
    assert double_char('.') == '..'


def test_double_char_9():
    assert double_char('aa') == 'aaaa'
```
