# get_sandwich




A sandwich is two pieces of bread with something in between. Return the string that is between the first and last appearance of "bread" in the given string, or return the empty string "" if there are not two pieces of bread.

```
get_sandwich("breadjambread") → "jam"
get_sandwich("xxbreadjambreadyy") → "jam"
get_sandwich("xxbreadyy") → ""
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p129952) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def get_sandwich(string: str) -> str:
    pass


result = get_sandwich('breadjambread')
print(result)
```

## Tests
```python
from main import get_sandwich


def test_get_sandwich_1():
    assert get_sandwich('breadjambread') == 'jam'


def test_get_sandwich_2():
    assert get_sandwich('xxbreadjambreadyy') == 'jam'


def test_get_sandwich_3():
    assert get_sandwich('xxbreadyy') == ''


def test_get_sandwich_4():
    assert get_sandwich('xxbreadbreadjambreadyy') == 'breadjam'


def test_get_sandwich_5():
    assert get_sandwich('breadAbread') == 'A'


def test_get_sandwich_6():
    assert get_sandwich('breadbread') == ''


def test_get_sandwich_7():
    assert get_sandwich('abcbreaz') == ''


def test_get_sandwich_8():
    assert get_sandwich('xyz') == ''


def test_get_sandwich_9():
    assert get_sandwich('') == ''


def test_get_sandwich_10():
    assert get_sandwich('breadbreaxbread') == 'breax'


def test_get_sandwich_11():
    assert get_sandwich('breaxbreadybread') == 'y'


def test_get_sandwich_12():
    assert get_sandwich('breadbreadbreadbread') == 'breadbread'
```
