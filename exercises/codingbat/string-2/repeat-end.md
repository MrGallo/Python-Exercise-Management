# repeat_end



**Requirements:**
```eval_rst
- :ref:`fundamentals:substrings and slicing`
- :ref:`fundamentals:loop with a counter variable`
- :ref:`fundamentals:string building and filtering`
- :ref:`fundamentals:returning a value`

```


Given a string and an int n, return a string made of n repetitions of the last n characters of the string. You may assume that n is between 0 and the length of the string, inclusive.

```
repeat_end("Hello", 3) -> "llollollo"
repeat_end("Hello", 2) -> "lolo"
repeat_end("Hello", 1) -> "o"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p152339) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def repeat_end(string: str, n: int) -> str:
    pass


result = repeat_end('Hello', 3)
print(result)
```

## Tests
```python
from main import repeat_end


def test_repeat_end_1():
    assert repeat_end('Hello', 3) == 'llollollo'


def test_repeat_end_2():
    assert repeat_end('Hello', 2) == 'lolo'


def test_repeat_end_3():
    assert repeat_end('Hello', 1) == 'o'


def test_repeat_end_4():
    assert repeat_end('Hello', 0) == ''


def test_repeat_end_5():
    assert repeat_end('abc', 3) == 'abcabcabc'


def test_repeat_end_6():
    assert repeat_end('1234', 2) == '3434'


def test_repeat_end_7():
    assert repeat_end('1234', 3) == '234234234'


def test_repeat_end_8():
    assert repeat_end('', 0) == ''
```
