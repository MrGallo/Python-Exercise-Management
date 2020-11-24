# n_twice
**Topic:** 



Given a string and an int n, return a string made of the first and last n chars from the string. The string length will be at least n.

<code>
n_twice("Hello", 2) → "Helo"
n_twice("Chocolate", 3) → "Choate"
n_twice("Chocolate", 1) → "Ce"
</code>

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p174148) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def n_twice(str: str, n: int) -> str:
```

## Tests
```python
from main import n_twice


def test_n_twice_1():
    assert n_twice('Hello', 2) == 'Helo'


def test_n_twice_2():
    assert n_twice('Chocolate', 3) == 'Choate'


def test_n_twice_3():
    assert n_twice('Chocolate', 1) == 'Ce'


def test_n_twice_4():
    assert n_twice('Chocolate', 0) == ''


def test_n_twice_5():
    assert n_twice('Hello', 4) == 'Hellello'


def test_n_twice_6():
    assert n_twice('Code', 4) == 'CodeCode'


def test_n_twice_7():
    assert n_twice('Code', 2) == 'Code'
```
