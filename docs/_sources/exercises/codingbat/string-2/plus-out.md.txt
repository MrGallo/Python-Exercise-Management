# plus_out
**Topic:** 



Given a string and a non-empty <b>word</b> string, return a version of the original String where all chars have been replaced by pluses ("+"), except for appearances of the word string which are preserved unchanged.

```
plus_out("12xy34", "xy") → "++xy++"
plus_out("12xy34", "1") → "1+++++"
plus_out("12xy34xyabcxy", "xy") → "++xy++xy+++xy"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p170829) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def plus_out(string: str, word: str) -> str:
```

## Tests
```python
from main import plus_out


def test_plus_out_1():
    assert plus_out('12xy34', 'xy') == '++xy++'


def test_plus_out_2():
    assert plus_out('12xy34', '1') == '1+++++'


def test_plus_out_3():
    assert plus_out('12xy34xyabcxy', 'xy') == '++xy++xy+++xy'


def test_plus_out_4():
    assert plus_out('abXYabcXYZ', 'ab') == 'ab++ab++++'


def test_plus_out_5():
    assert plus_out('abXYabcXYZ', 'abc') == '++++abc+++'


def test_plus_out_6():
    assert plus_out('abXYabcXYZ', 'XY') == '++XY+++XY+'


def test_plus_out_7():
    assert plus_out('abXYxyzXYZ', 'XYZ') == '+++++++XYZ'


def test_plus_out_8():
    assert plus_out('--++ab', '++') == '++++++'


def test_plus_out_9():
    assert plus_out('aaxxxxbb', 'xx') == '++xxxx++'


def test_plus_out_10():
    assert plus_out('123123', '3') == '++3++3'
```
