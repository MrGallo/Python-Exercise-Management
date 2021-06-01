# count_abc





Count recursively the total number of "abc" and "aba" substrings that appear in the given string.

```
count_abc("abc") -> 1
count_abc("abcxxabc") -> 2
count_abc("abaxxaba") -> 2
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p161124) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def count_abc(string: str) -> int:
    pass


result = count_abc('abc')
print(result)
```

## Tests
```python
from main import count_abc


def test_count_abc_1():
    assert count_abc('abc') == 1


def test_count_abc_2():
    assert count_abc('abcxxabc') == 2


def test_count_abc_3():
    assert count_abc('abaxxaba') == 2


def test_count_abc_4():
    assert count_abc('ababc') == 2


def test_count_abc_5():
    assert count_abc('abxbc') == 0


def test_count_abc_6():
    assert count_abc('aaabc') == 1


def test_count_abc_7():
    assert count_abc('hello') == 0


def test_count_abc_8():
    assert count_abc('') == 0


def test_count_abc_9():
    assert count_abc('ab') == 0


def test_count_abc_10():
    assert count_abc('aba') == 1


def test_count_abc_11():
    assert count_abc('aca') == 0


def test_count_abc_12():
    assert count_abc('aaa') == 0
```
