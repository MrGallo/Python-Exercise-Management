# make_out_word





Given an "out" string length 4, such as "&lt;&lt;&gt;&gt;", and a word, return a new string where the word is in the middle of the out string, e.g. "&lt;&lt;word&gt;&gt;". Note: use `str[i:j]` to extract the String starting at index i and going up to but not including index j.

```
make_out_word("&lt;&lt;&gt;&gt;", "Yay") â†’ "&lt;&lt;Yay&gt;&gt;"
make_out_word("&lt;&lt;&gt;&gt;", "WooHoo") â†’ "&lt;&lt;WooHoo&gt;&gt;"
make_out_word("[[]]", "word") â†’ "[[word]]"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p184030) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def make_out_word(out: str, word: str) -> str:
    pass


result = make_out_word('<<>>', 'Yay')
print(result)
```

## Tests
```python
from main import make_out_word


def test_make_out_word_1():
    assert make_out_word('<<>>', 'Yay') == '<<Yay>>'


def test_make_out_word_2():
    assert make_out_word('<<>>', 'WooHoo') == '<<WooHoo>>'


def test_make_out_word_3():
    assert make_out_word('[[]]', 'word') == '[[word]]'


def test_make_out_word_4():
    assert make_out_word('HHoo', 'Hello') == 'HHHellooo'


def test_make_out_word_5():
    assert make_out_word('abyz', 'YAY') == 'abYAYyz'
```
