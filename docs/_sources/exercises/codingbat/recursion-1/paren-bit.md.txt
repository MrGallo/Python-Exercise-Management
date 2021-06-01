# paren_bit





Given a string that contains a single pair of parenthesis, compute recursively a new string made of only of the parenthesis and their contents, so "xyz(abc)123" yields "(abc)".

```
paren_bit("xyz(abc)123") -> "(abc)"
paren_bit("x(hello)") -> "(hello)"
paren_bit("(xy)1") -> "(xy)"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p137918) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def paren_bit(string: str) -> str:
    pass


result = paren_bit('xyz(abc)123')
print(result)
```

## Tests
```python
from main import paren_bit


def test_paren_bit_1():
    assert paren_bit('xyz(abc)123') == '(abc)'


def test_paren_bit_2():
    assert paren_bit('x(hello)') == '(hello)'


def test_paren_bit_3():
    assert paren_bit('(xy)1') == '(xy)'


def test_paren_bit_4():
    assert paren_bit('not really (possible)') == '(possible)'


def test_paren_bit_5():
    assert paren_bit('(abc)') == '(abc)'


def test_paren_bit_6():
    assert paren_bit('(abc)xyz') == '(abc)'


def test_paren_bit_7():
    assert paren_bit('(abc)x') == '(abc)'


def test_paren_bit_8():
    assert paren_bit('(x)') == '(x)'


def test_paren_bit_9():
    assert paren_bit('()') == '()'


def test_paren_bit_10():
    assert paren_bit('res (ipsa) loquitor') == '(ipsa)'


def test_paren_bit_11():
    assert paren_bit('hello(not really)there') == '(not really)'


def test_paren_bit_12():
    assert paren_bit('ab(ab)ab') == '(ab)'
```
