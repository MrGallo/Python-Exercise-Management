# start_word





Given a string and a second "word" string, we'll say that the word matches the string if it appears at the front of the string, except its first char does not need to match exactly. On a match, return the front of the string, or otherwise return the empty string. So, so with the string "hippo" the word "hi" returns "hi" and "xip" returns "hip". The word will be at least length 1.

```
start_word("hippo", "hi") â†’ "hi"
start_word("hippo", "xip") â†’ "hip"
start_word("hippo", "i") â†’ "h"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p141494) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def start_word(string: str, word: str) -> str:
    pass


result = start_word('hippo', 'hi')
print(result)
```

## Tests
```python
from main import start_word


def test_start_word_1():
    assert start_word('hippo', 'hi') == 'hi'


def test_start_word_2():
    assert start_word('hippo', 'xip') == 'hip'


def test_start_word_3():
    assert start_word('hippo', 'i') == 'h'


def test_start_word_4():
    assert start_word('hippo', 'ix') == ''


def test_start_word_5():
    assert start_word('h', 'ix') == ''


def test_start_word_6():
    assert start_word('', 'i') == ''


def test_start_word_7():
    assert start_word('hip', 'zi') == 'hi'


def test_start_word_8():
    assert start_word('hip', 'zip') == 'hip'


def test_start_word_9():
    assert start_word('hip', 'zig') == ''


def test_start_word_10():
    assert start_word('h', 'z') == 'h'


def test_start_word_11():
    assert start_word('hippo', 'xippo') == 'hippo'


def test_start_word_12():
    assert start_word('hippo', 'xyz') == ''


def test_start_word_13():
    assert start_word('hippo', 'hip') == 'hip'


def test_start_word_14():
    assert start_word('kitten', 'cit') == 'kit'


def test_start_word_15():
    assert start_word('kit', 'cit') == 'kit'
```
