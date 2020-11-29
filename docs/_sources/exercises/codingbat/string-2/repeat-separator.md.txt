# repeat_separator



**Requirements:**
```eval_rst
- :ref:`fundamentals:if, else`
- :ref:`fundamentals:loop with a counter variable`
- :ref:`fundamentals:string building and filtering`
- :ref:`fundamentals:returning a value`

```


Given two strings, <b>word</b> and a separator <b>sep</b>, return a big string made of <b>count</b> occurrences of the word, separated by the separator string.

```
repeat_separator("Word", "X", 3) -> "WordXWordXWord"
repeat_separator("This", "And", 2) -> "ThisAndThis"
repeat_separator("This", "And", 1) -> "This"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p109637) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def repeat_separator(word: str, sep: str, count: int) -> str:
    pass


result = repeat_separator('Word', 'X', 3)
print(result)
```

## Tests
```python
from main import repeat_separator


def test_repeat_separator_1():
    assert repeat_separator('Word', 'X', 3) == 'WordXWordXWord'


def test_repeat_separator_2():
    assert repeat_separator('This', 'And', 2) == 'ThisAndThis'


def test_repeat_separator_3():
    assert repeat_separator('This', 'And', 1) == 'This'


def test_repeat_separator_4():
    assert repeat_separator('Hi', '-n-', 2) == 'Hi-n-Hi'


def test_repeat_separator_5():
    assert repeat_separator('AAA', '', 1) == 'AAA'


def test_repeat_separator_6():
    assert repeat_separator('AAA', '', 0) == ''


def test_repeat_separator_7():
    assert repeat_separator('A', 'B', 5) == 'ABABABABA'


def test_repeat_separator_8():
    assert repeat_separator('abc', 'XX', 3) == 'abcXXabcXXabc'


def test_repeat_separator_9():
    assert repeat_separator('abc', 'XX', 2) == 'abcXXabc'


def test_repeat_separator_10():
    assert repeat_separator('abc', 'XX', 1) == 'abc'


def test_repeat_separator_11():
    assert repeat_separator('XYZ', 'a', 2) == 'XYZaXYZ'
```
