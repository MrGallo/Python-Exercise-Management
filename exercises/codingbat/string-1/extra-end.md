# extra_end





Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.

```
extra_end("Hello") â†’ "lololo"
extra_end("ab") â†’ "ababab"
extra_end("Hi") â†’ "HiHiHi"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p108853) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def extra_end(string: str) -> str:
    pass


result = extra_end('Hello')
print(result)
```

## Tests
```python
from main import extra_end


def test_extra_end_1():
    assert extra_end('Hello') == 'lololo'


def test_extra_end_2():
    assert extra_end('ab') == 'ababab'


def test_extra_end_3():
    assert extra_end('Hi') == 'HiHiHi'


def test_extra_end_4():
    assert extra_end('Candy') == 'dydydy'


def test_extra_end_5():
    assert extra_end('Code') == 'dedede'
```
