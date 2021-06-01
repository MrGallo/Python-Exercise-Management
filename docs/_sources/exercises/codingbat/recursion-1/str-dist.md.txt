# str_dist





Given a string and a non-empty substring <b>sub</b>, compute recursively the largest substring which starts and ends with sub and return its length.

```
str_dist("catcowcat", "cat") -> 9
str_dist("catcowcat", "cow") -> 3
str_dist("cccatcowcatxx", "cat") -> 9
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p195413) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def str_dist(string: str, sub: str) -> int:
    pass


result = str_dist('catcowcat', 'cat')
print(result)
```

## Tests
```python
from main import str_dist


def test_str_dist_1():
    assert str_dist('catcowcat', 'cat') == 9


def test_str_dist_2():
    assert str_dist('catcowcat', 'cow') == 3


def test_str_dist_3():
    assert str_dist('cccatcowcatxx', 'cat') == 9


def test_str_dist_4():
    assert str_dist('abccatcowcatcatxyz', 'cat') == 12


def test_str_dist_5():
    assert str_dist('xyx', 'x') == 3


def test_str_dist_6():
    assert str_dist('xyx', 'y') == 1


def test_str_dist_7():
    assert str_dist('xyx', 'z') == 0


def test_str_dist_8():
    assert str_dist('z', 'z') == 1


def test_str_dist_9():
    assert str_dist('x', 'z') == 0


def test_str_dist_10():
    assert str_dist('', 'z') == 0


def test_str_dist_11():
    assert str_dist('hiHellohihihi', 'hi') == 13


def test_str_dist_12():
    assert str_dist('hiHellohihihi', 'hih') == 5


def test_str_dist_13():
    assert str_dist('hiHellohihihi', 'o') == 1


def test_str_dist_14():
    assert str_dist('hiHellohihihi', 'll') == 2
```
