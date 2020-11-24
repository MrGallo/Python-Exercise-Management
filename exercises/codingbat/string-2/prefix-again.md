# prefix_again
**Topic:** 



Given a string, consider the prefix string made of the first N chars of the string. Does that prefix string appear somewhere else in the string? Assume that the string is not empty and that N is in the range 1..str.length().

```
prefix_again("abXYabc", 1) → true
prefix_again("abXYabc", 2) → true
prefix_again("abXYabc", 3) → false
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p136417) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def prefix_again(string: str, n: int) -> bool:
```

## Tests
```python
from main import prefix_again


def test_prefix_again_1():
    assert prefix_again('abXYabc', 1) == True


def test_prefix_again_2():
    assert prefix_again('abXYabc', 2) == True


def test_prefix_again_3():
    assert prefix_again('abXYabc', 3) == False


def test_prefix_again_4():
    assert prefix_again('xyzxyxyxy', 2) == True


def test_prefix_again_5():
    assert prefix_again('xyzxyxyxy', 3) == False


def test_prefix_again_6():
    assert prefix_again('Hi12345Hi6789Hi10', 1) == True


def test_prefix_again_7():
    assert prefix_again('Hi12345Hi6789Hi10', 2) == True


def test_prefix_again_8():
    assert prefix_again('Hi12345Hi6789Hi10', 3) == True


def test_prefix_again_9():
    assert prefix_again('Hi12345Hi6789Hi10', 4) == False


def test_prefix_again_10():
    assert prefix_again('a', 1) == False


def test_prefix_again_11():
    assert prefix_again('aa', 1) == True


def test_prefix_again_12():
    assert prefix_again('ab', 1) == False
```
