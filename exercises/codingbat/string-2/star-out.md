# star_out
**Topic:** 



Return a version of the given string, where for every star (*) in the string the star and the chars immediately to its left and right are gone. So "ab*cd" yields "ad" and "ab**cd" also yields "ad".

```
star_out("ab*cd") → "ad"
star_out("ab**cd") → "ad"
star_out("sm*eilly") → "silly"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p139564) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def star_out(str: str) -> str:
```

## Tests
```python
from main import star_out


def test_star_out_1():
    assert star_out('ab*cd') == 'ad'


def test_star_out_2():
    assert star_out('ab**cd') == 'ad'


def test_star_out_3():
    assert star_out('sm*eilly') == 'silly'


def test_star_out_4():
    assert star_out('sm*eil*ly') == 'siy'


def test_star_out_5():
    assert star_out('sm**eil*ly') == 'siy'


def test_star_out_6():
    assert star_out('sm***eil*ly') == 'siy'


def test_star_out_7():
    assert star_out('stringy*') == 'string'


def test_star_out_8():
    assert star_out('*stringy') == 'tringy'


def test_star_out_9():
    assert star_out('*str*in*gy') == 'ty'


def test_star_out_10():
    assert star_out('abc') == 'abc'


def test_star_out_11():
    assert star_out('a*bc') == 'c'


def test_star_out_12():
    assert star_out('ab') == 'ab'


def test_star_out_13():
    assert star_out('a*b') == ''


def test_star_out_14():
    assert star_out('a') == 'a'


def test_star_out_15():
    assert star_out('a*') == ''


def test_star_out_16():
    assert star_out('*a') == ''


def test_star_out_17():
    assert star_out('*') == ''


def test_star_out_18():
    assert star_out('') == ''
```
