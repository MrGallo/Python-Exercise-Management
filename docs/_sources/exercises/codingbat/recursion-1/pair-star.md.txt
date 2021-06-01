# pair_star





Given a string, compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a "*".

```
pair_star("hello") -> "hel*lo"
pair_star("xxyy") -> "x*xy*y"
pair_star("aaaa") -> "a*a*a*a"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p158175) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def pair_star(string: str) -> str:
    pass


result = pair_star('hello')
print(result)
```

## Tests
```python
from main import pair_star


def test_pair_star_1():
    assert pair_star('hello') == 'hel*lo'


def test_pair_star_2():
    assert pair_star('xxyy') == 'x*xy*y'


def test_pair_star_3():
    assert pair_star('aaaa') == 'a*a*a*a'


def test_pair_star_4():
    assert pair_star('aaab') == 'a*a*ab'


def test_pair_star_5():
    assert pair_star('aa') == 'a*a'


def test_pair_star_6():
    assert pair_star('a') == 'a'


def test_pair_star_7():
    assert pair_star('') == ''


def test_pair_star_8():
    assert pair_star('noadjacent') == 'noadjacent'


def test_pair_star_9():
    assert pair_star('abba') == 'ab*ba'


def test_pair_star_10():
    assert pair_star('abbba') == 'ab*b*ba'
```
