# one_two





Given a string, compute a new string by moving the first char to come after the next two chars, so "abc" yields "bca". Repeat this process for each subsequent group of 3 chars, so "abcdef" yields "bcaefd". Ignore any group of fewer than 3 chars at the end.

```
one_two("abc") → "bca"
one_two("tca") → "cat"
one_two("tcagdo") → "catdog"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p122943) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def one_two(string: str) -> str:
    pass


result = one_two('abc')
print(result)
```

## Tests
```python
from main import one_two


def test_one_two_1():
    assert one_two('abc') == 'bca'


def test_one_two_2():
    assert one_two('tca') == 'cat'


def test_one_two_3():
    assert one_two('tcagdo') == 'catdog'


def test_one_two_4():
    assert one_two('chocolate') == 'hocolctea'


def test_one_two_5():
    assert one_two('1234567890') == '231564897'


def test_one_two_6():
    assert one_two('xabxabxabxabxabxabxab') == 'abxabxabxabxabxabxabx'


def test_one_two_7():
    assert one_two('abcdefx') == 'bcaefd'


def test_one_two_8():
    assert one_two('abcdefxy') == 'bcaefd'


def test_one_two_9():
    assert one_two('abcdefxyz') == 'bcaefdyzx'


def test_one_two_10():
    assert one_two('') == ''


def test_one_two_11():
    assert one_two('x') == ''


def test_one_two_12():
    assert one_two('xy') == ''


def test_one_two_13():
    assert one_two('xyz') == 'yzx'


def test_one_two_14():
    assert one_two('abcdefghijklkmnopqrstuvwxyz1234567890') == 'bcaefdhigkljmnkpqostrvwuyzx231564897'


def test_one_two_15():
    assert one_two('abcdefghijklkmnopqrstuvwxyz123456789') == 'bcaefdhigkljmnkpqostrvwuyzx231564897'


def test_one_two_16():
    assert one_two('abcdefghijklkmnopqrstuvwxyz12345678') == 'bcaefdhigkljmnkpqostrvwuyzx231564'
```
