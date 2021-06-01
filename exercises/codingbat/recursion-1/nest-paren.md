# nest_paren





Given a string, return true if it is a nesting of zero or more pairs of parenthesis, like "(())" or "((()))". Suggestion: check the first and last chars, and then recur on what's inside them.

```
nest_paren("(())") -> true
nest_paren("((()))") -> true
nest_paren("(((x))") -> false
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p183174) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def nest_paren(string: str) -> bool:
    pass


result = nest_paren('(())')
print(result)
```

## Tests
```python
from main import nest_paren


def test_nest_paren_1():
    assert nest_paren('(())') == True


def test_nest_paren_2():
    assert nest_paren('((()))') == True


def test_nest_paren_3():
    assert nest_paren('(((x))') == False


def test_nest_paren_4():
    assert nest_paren('((())') == False


def test_nest_paren_5():
    assert nest_paren('((()()') == False


def test_nest_paren_6():
    assert nest_paren('()') == True


def test_nest_paren_7():
    assert nest_paren('') == True


def test_nest_paren_8():
    assert nest_paren('(yy)') == False


def test_nest_paren_9():
    assert nest_paren('(())') == True


def test_nest_paren_10():
    assert nest_paren('(((y))') == False


def test_nest_paren_11():
    assert nest_paren('((y)))') == False


def test_nest_paren_12():
    assert nest_paren('((()))') == True


def test_nest_paren_13():
    assert nest_paren('(())))') == False


def test_nest_paren_14():
    assert nest_paren('((yy())))') == False


def test_nest_paren_15():
    assert nest_paren('(((())))') == True
```
