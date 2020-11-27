# word_ends





Given a string and a non-empty <b>word</b> string, return a string made of each char just before and just after every appearance of the word in the string. Ignore cases where there is no char before or after the word, and a char may be included twice if it is between two words.

```
word_ends("abcXY123XYijk", "XY") → "c13i"
word_ends("XY123XY", "XY") → "13"
word_ends("XY1XY", "XY") → "11"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p147538) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def word_ends(string: str, word: str) -> str:
    pass


result = word_ends('abcXY123XYijk', 'XY')
print(result)
```

## Tests
```python
from main import word_ends


def test_word_ends_1():
    assert word_ends('abcXY123XYijk', 'XY') == 'c13i'


def test_word_ends_2():
    assert word_ends('XY123XY', 'XY') == '13'


def test_word_ends_3():
    assert word_ends('XY1XY', 'XY') == '11'


def test_word_ends_4():
    assert word_ends('XYXY', 'XY') == 'XY'


def test_word_ends_5():
    assert word_ends('XY', 'XY') == ''


def test_word_ends_6():
    assert word_ends('Hi', 'XY') == ''


def test_word_ends_7():
    assert word_ends('', 'XY') == ''


def test_word_ends_8():
    assert word_ends('abc1xyz1i1j', '1') == 'cxziij'


def test_word_ends_9():
    assert word_ends('abc1xyz1', '1') == 'cxz'


def test_word_ends_10():
    assert word_ends('abc1xyz11', '1') == 'cxz11'


def test_word_ends_11():
    assert word_ends('abc1xyz1abc', 'abc') == '11'


def test_word_ends_12():
    assert word_ends('abc1xyz1abc', 'b') == 'acac'


def test_word_ends_13():
    assert word_ends('abc1abc1abc', 'abc') == '1111'
```
