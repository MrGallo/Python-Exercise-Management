# min_cat





Given two strings, append them together (known as "concatenation") and return the result. However, if the strings are different lengths, omit chars from the longer string so it is the same length as the shorter string. So "Hello" and "Hi" yield "loHi". The strings may be any length.

```
min_cat("Hello", "Hi") -> "loHi"
min_cat("Hello", "java") -> "ellojava"
min_cat("java", "Hello") -> "javaello"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p105745) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def min_cat(a: str, b: str) -> str:
    pass


result = min_cat('Hello', 'Hi')
print(result)
```

## Tests
```python
from main import min_cat


def test_min_cat_1():
    assert min_cat('Hello', 'Hi') == 'loHi'


def test_min_cat_2():
    assert min_cat('Hello', 'java') == 'ellojava'


def test_min_cat_3():
    assert min_cat('java', 'Hello') == 'javaello'


def test_min_cat_4():
    assert min_cat('abc', 'x') == 'cx'


def test_min_cat_5():
    assert min_cat('x', 'abc') == 'xc'


def test_min_cat_6():
    assert min_cat('abc', '') == ''
```
