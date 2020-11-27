# start_oz





Given a string, return a string made of the first 2 chars (if present), however include first char only if it is 'o' and include the second only if it is 'z', so "ozymandias" yields "oz".

```
start_oz("ozymandias") → "oz"
start_oz("bzoo") → "z"
start_oz("oxx") → "o"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p199720) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def start_oz(string: str) -> str:
    pass


result = start_oz('ozymandias')
print(result)
```

## Tests
```python
from main import start_oz


def test_start_oz_1():
    assert start_oz('ozymandias') == 'oz'


def test_start_oz_2():
    assert start_oz('bzoo') == 'z'


def test_start_oz_3():
    assert start_oz('oxx') == 'o'


def test_start_oz_4():
    assert start_oz('oz') == 'oz'


def test_start_oz_5():
    assert start_oz('ounce') == 'o'


def test_start_oz_6():
    assert start_oz('o') == 'o'


def test_start_oz_7():
    assert start_oz('abc') == ''


def test_start_oz_8():
    assert start_oz('') == ''


def test_start_oz_9():
    assert start_oz('zoo') == ''


def test_start_oz_10():
    assert start_oz('aztec') == 'z'


def test_start_oz_11():
    assert start_oz('zzzz') == 'z'


def test_start_oz_12():
    assert start_oz('oznic') == 'oz'
```
