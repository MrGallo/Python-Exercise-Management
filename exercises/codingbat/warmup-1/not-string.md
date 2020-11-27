# not_string





Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged. Note: use .equals() to compare 2 strings.

```
not_string("candy") â†’ "not candy"
not_string("x") â†’ "not x"
not_string("not bad") â†’ "not bad"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p191914) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def not_string(string: str) -> str:
    pass


result = not_string('candy')
print(result)
```

## Tests
```python
from main import not_string


def test_not_string_1():
    assert not_string('candy') == 'not candy'


def test_not_string_2():
    assert not_string('x') == 'not x'


def test_not_string_3():
    assert not_string('not bad') == 'not bad'


def test_not_string_4():
    assert not_string('bad') == 'not bad'


def test_not_string_5():
    assert not_string('not') == 'not'


def test_not_string_6():
    assert not_string('is not') == 'not is not'


def test_not_string_7():
    assert not_string('no') == 'not no'
```
