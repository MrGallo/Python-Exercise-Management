# de_front
**Topic:** 



Given a string, return a version without the first 2 chars. Except keep the first char if it is 'a' and keep the second char if it is 'b'. The string may be any length. Harder than it looks.

<code>
de_front("Hello") → "llo"
de_front("java") → "va"
de_front("away") → "aay"
</code>

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p110141) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def de_front(str: str) -> str:
```

## Tests
```python
from main import de_front


def test_de_front_1():
    assert de_front('Hello') == 'llo'


def test_de_front_2():
    assert de_front('java') == 'va'


def test_de_front_3():
    assert de_front('away') == 'aay'


def test_de_front_4():
    assert de_front('axy') == 'ay'


def test_de_front_5():
    assert de_front('abc') == 'abc'


def test_de_front_6():
    assert de_front('xby') == 'by'


def test_de_front_7():
    assert de_front('ab') == 'ab'


def test_de_front_8():
    assert de_front('ax') == 'a'


def test_de_front_9():
    assert de_front('axb') == 'ab'


def test_de_front_10():
    assert de_front('aaa') == 'aa'


def test_de_front_11():
    assert de_front('xbc') == 'bc'


def test_de_front_12():
    assert de_front('bbb') == 'bb'


def test_de_front_13():
    assert de_front('bazz') == 'zz'


def test_de_front_14():
    assert de_front('ba') == ''


def test_de_front_15():
    assert de_front('abxyz') == 'abxyz'


def test_de_front_16():
    assert de_front('hi') == ''


def test_de_front_17():
    assert de_front('his') == 's'


def test_de_front_18():
    assert de_front('xz') == ''


def test_de_front_19():
    assert de_front('zzz') == 'z'
```
