# combo_string
**Topic:** 



Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).

<code>
combo_string("Hello", "hi") → "hiHellohi"
combo_string("hi", "Hello") → "hiHellohi"
combo_string("aaa", "b") → "baaab"
</code>

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p168564) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def combo_string(a: str, b: str) -> str:
```

## Tests
```python
from main import combo_string


def test_combo_string_1():
    assert combo_string('Hello', 'hi') == 'hiHellohi'


def test_combo_string_2():
    assert combo_string('hi', 'Hello') == 'hiHellohi'


def test_combo_string_3():
    assert combo_string('aaa', 'b') == 'baaab'


def test_combo_string_4():
    assert combo_string('b', 'aaa') == 'baaab'


def test_combo_string_5():
    assert combo_string('aaa', '') == 'aaa'


def test_combo_string_6():
    assert combo_string('', 'bb') == 'bb'


def test_combo_string_7():
    assert combo_string('aaa', '1234') == 'aaa1234aaa'


def test_combo_string_8():
    assert combo_string('aaa', 'bb') == 'bbaaabb'


def test_combo_string_9():
    assert combo_string('a', 'bb') == 'abba'


def test_combo_string_10():
    assert combo_string('bb', 'a') == 'abba'


def test_combo_string_11():
    assert combo_string('xyz', 'ab') == 'abxyzab'
```
