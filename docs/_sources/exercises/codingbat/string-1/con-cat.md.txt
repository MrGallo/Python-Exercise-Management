# con_cat
**Topic:** 



Given two strings, append them together (known as "concatenation") and return the result. However, if the concatenation creates a double-char, then omit one of the chars, so "abc" and "cat" yields "abcat".

<code>
con_cat("abc", "cat") → "abcat"
con_cat("dog", "cat") → "dogcat"
con_cat("abc", "") → "abc"
</code>

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p132118) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def con_cat(a: str, b: str) -> str:
```

## Tests
```python
from main import con_cat


def test_con_cat_1():
    assert con_cat('abc', 'cat') == 'abcat'


def test_con_cat_2():
    assert con_cat('dog', 'cat') == 'dogcat'


def test_con_cat_3():
    assert con_cat('abc', '') == 'abc'


def test_con_cat_4():
    assert con_cat('', 'cat') == 'cat'


def test_con_cat_5():
    assert con_cat('pig', 'g') == 'pig'


def test_con_cat_6():
    assert con_cat('pig', 'doggy') == 'pigdoggy'
```
