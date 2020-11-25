# last_two




Given a string of any length, return a new string where the last 2 chars, if present, are swapped, so "coding" yields "codign".

```
last_two("coding") → "codign"
last_two("cat") → "cta"
last_two("ab") → "ba"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p194786) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def last_two(string: str) -> str:
    pass


result = last_two('coding')
print(result)
```

## Tests
```python
from main import last_two


def test_last_two_1():
    assert last_two('coding') == 'codign'


def test_last_two_2():
    assert last_two('cat') == 'cta'


def test_last_two_3():
    assert last_two('ab') == 'ba'


def test_last_two_4():
    assert last_two('a') == 'a'


def test_last_two_5():
    assert last_two('') == ''
```
