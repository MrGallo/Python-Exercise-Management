# end_x





Given a string, compute recursively a new string where all the lowercase 'x' chars have been moved to the end of the string.

```
end_x("xxre") -> "rexx"
end_x("xxhixx") -> "hixxxx"
end_x("xhixhix") -> "hihixxx"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p105722) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def end_x(string: str) -> str:
    pass


result = end_x('xxre')
print(result)
```

## Tests
```python
from main import end_x


def test_end_x_1():
    assert end_x('xxre') == 'rexx'


def test_end_x_2():
    assert end_x('xxhixx') == 'hixxxx'


def test_end_x_3():
    assert end_x('xhixhix') == 'hihixxx'


def test_end_x_4():
    assert end_x('hiy') == 'hiy'


def test_end_x_5():
    assert end_x('h') == 'h'


def test_end_x_6():
    assert end_x('x') == 'x'


def test_end_x_7():
    assert end_x('xx') == 'xx'


def test_end_x_8():
    assert end_x('') == ''


def test_end_x_9():
    assert end_x('bxx') == 'bxx'


def test_end_x_10():
    assert end_x('bxax') == 'baxx'


def test_end_x_11():
    assert end_x('axaxax') == 'aaaxxx'


def test_end_x_12():
    assert end_x('xxhxi') == 'hixxx'
```
