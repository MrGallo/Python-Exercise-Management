# str_count





Given a string and a non-empty substring <b>sub</b>, compute recursively the number of times that sub appears in the string, without the sub strings overlapping.

```
str_count("catcowcat", "cat") -> 2
str_count("catcowcat", "cow") -> 1
str_count("catcowcat", "dog") -> 0
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p186177) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def str_count(string: str, sub: str) -> int:
    pass


result = str_count('catcowcat', 'cat')
print(result)
```

## Tests
```python
from main import str_count


def test_str_count_1():
    assert str_count('catcowcat', 'cat') == 2


def test_str_count_2():
    assert str_count('catcowcat', 'cow') == 1


def test_str_count_3():
    assert str_count('catcowcat', 'dog') == 0


def test_str_count_4():
    assert str_count('cacatcowcat', 'cat') == 2


def test_str_count_5():
    assert str_count('xyx', 'x') == 2


def test_str_count_6():
    assert str_count('iiiijj', 'i') == 4


def test_str_count_7():
    assert str_count('iiiijj', 'ii') == 2


def test_str_count_8():
    assert str_count('iiiijj', 'iii') == 1


def test_str_count_9():
    assert str_count('iiiijj', 'j') == 2


def test_str_count_10():
    assert str_count('iiiijj', 'jj') == 1


def test_str_count_11():
    assert str_count('aaabababab', 'ab') == 4


def test_str_count_12():
    assert str_count('aaabababab', 'aa') == 1


def test_str_count_13():
    assert str_count('aaabababab', 'a') == 6


def test_str_count_14():
    assert str_count('aaabababab', 'b') == 4
```
