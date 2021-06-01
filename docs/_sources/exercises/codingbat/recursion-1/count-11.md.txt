# count_11





Given a string, compute recursively (no loops) the number of "11" substrings in the string. The "11" substrings should not overlap.

```
count_11("11abc11") -> 2
count_11("abc11x11x11") -> 3
count_11("111") -> 1
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p167015) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def count_11(string: str) -> int:
    pass


result = count_11('11abc11')
print(result)
```

## Tests
```python
from main import count_11


def test_count_11_1():
    assert count_11('11abc11') == 2


def test_count_11_2():
    assert count_11('abc11x11x11') == 3


def test_count_11_3():
    assert count_11('111') == 1


def test_count_11_4():
    assert count_11('1111') == 2


def test_count_11_5():
    assert count_11('1') == 0


def test_count_11_6():
    assert count_11('') == 0


def test_count_11_7():
    assert count_11('hi') == 0


def test_count_11_8():
    assert count_11('11x111x1111') == 4


def test_count_11_9():
    assert count_11('1x111') == 1


def test_count_11_10():
    assert count_11('1Hello1') == 0


def test_count_11_11():
    assert count_11('Hello') == 0
```
