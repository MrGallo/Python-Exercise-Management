# count_x





Given a string, compute recursively (no loops) the number of lowercase 'x' chars in the string.

```
count_x("xxhixx") -> 4
count_x("xhixhix") -> 3
count_x("hi") -> 0
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p170371) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def count_x(string: str) -> int:
    pass


result = count_x('xxhixx')
print(result)
```

## Tests
```python
from main import count_x


def test_count_x_1():
    assert count_x('xxhixx') == 4


def test_count_x_2():
    assert count_x('xhixhix') == 3


def test_count_x_3():
    assert count_x('hi') == 0


def test_count_x_4():
    assert count_x('h') == 0


def test_count_x_5():
    assert count_x('x') == 1


def test_count_x_6():
    assert count_x('') == 0


def test_count_x_7():
    assert count_x('hihi') == 0


def test_count_x_8():
    assert count_x('hiAAhi12hi') == 0
```
