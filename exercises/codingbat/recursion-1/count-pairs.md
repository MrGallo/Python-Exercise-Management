# count_pairs





We'll say that a "pair" in a string is two instances of a char separated by a char. So "AxA" the A's make a pair. Pair's can overlap, so "AxAxA" contains 3 pairs -- 2 for A and 1 for x. Recursively compute the number of pairs in the given string.

```
count_pairs("axa") -> 1
count_pairs("axax") -> 2
count_pairs("axbx") -> 1
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p154048) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def count_pairs(string: str) -> int:
    pass


result = count_pairs('axa')
print(result)
```

## Tests
```python
from main import count_pairs


def test_count_pairs_1():
    assert count_pairs('axa') == 1


def test_count_pairs_2():
    assert count_pairs('axax') == 2


def test_count_pairs_3():
    assert count_pairs('axbx') == 1


def test_count_pairs_4():
    assert count_pairs('hi') == 0


def test_count_pairs_5():
    assert count_pairs('hihih') == 3


def test_count_pairs_6():
    assert count_pairs('ihihhh') == 3


def test_count_pairs_7():
    assert count_pairs('ihjxhh') == 0


def test_count_pairs_8():
    assert count_pairs('') == 0


def test_count_pairs_9():
    assert count_pairs('a') == 0


def test_count_pairs_10():
    assert count_pairs('aa') == 0


def test_count_pairs_11():
    assert count_pairs('aaa') == 1
```
