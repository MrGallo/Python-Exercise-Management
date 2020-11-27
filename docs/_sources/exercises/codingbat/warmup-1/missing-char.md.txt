# missing_char





Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..str.length()-1 inclusive).

```
missing_char("kitten", 1) → "ktten"
missing_char("kitten", 0) → "itten"
missing_char("kitten", 4) → "kittn"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p190570) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def missing_char(string: str, n: int) -> str:
    pass


result = missing_char('kitten', 1)
print(result)
```

## Tests
```python
from main import missing_char


def test_missing_char_1():
    assert missing_char('kitten', 1) == 'ktten'


def test_missing_char_2():
    assert missing_char('kitten', 0) == 'itten'


def test_missing_char_3():
    assert missing_char('kitten', 4) == 'kittn'


def test_missing_char_4():
    assert missing_char('Hi', 0) == 'i'


def test_missing_char_5():
    assert missing_char('Hi', 1) == 'H'


def test_missing_char_6():
    assert missing_char('code', 0) == 'ode'


def test_missing_char_7():
    assert missing_char('code', 1) == 'cde'


def test_missing_char_8():
    assert missing_char('code', 2) == 'coe'


def test_missing_char_9():
    assert missing_char('code', 3) == 'cod'


def test_missing_char_10():
    assert missing_char('chocolate', 8) == 'chocolat'
```
