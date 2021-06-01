# string_clean





Given a string, return recursively a "cleaned" string where adjacent chars that are the same have been reduced to a single char. So "yyzzza" yields "yza".

```
string_clean("yyzzza") -> "yza"
string_clean("abbbcdd") -> "abcd"
string_clean("Hello") -> "Helo"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p104029) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def string_clean(string: str) -> str:
    pass


result = string_clean('yyzzza')
print(result)
```

## Tests
```python
from main import string_clean


def test_string_clean_1():
    assert string_clean('yyzzza') == 'yza'


def test_string_clean_2():
    assert string_clean('abbbcdd') == 'abcd'


def test_string_clean_3():
    assert string_clean('Hello') == 'Helo'


def test_string_clean_4():
    assert string_clean('XXabcYY') == 'XabcY'


def test_string_clean_5():
    assert string_clean('112ab445') == '12ab45'


def test_string_clean_6():
    assert string_clean('Hello Bookkeeper') == 'Helo Bokeper'
```
