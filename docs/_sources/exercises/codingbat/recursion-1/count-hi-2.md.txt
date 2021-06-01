# count_hi_2





Given a string, compute recursively the number of times lowercase "hi" appears in the string, however do not count "hi" that have an 'x' immedately before them.

```
count_hi_2("ahixhi") -> 1
count_hi_2("ahibhi") -> 2
count_hi_2("xhixhi") -> 0
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p143900) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def count_hi_2(string: str) -> int:
    pass


result = count_hi_2('ahixhi')
print(result)
```

## Tests
```python
from main import count_hi_2


def test_count_hi_2_1():
    assert count_hi_2('ahixhi') == 1


def test_count_hi_2_2():
    assert count_hi_2('ahibhi') == 2


def test_count_hi_2_3():
    assert count_hi_2('xhixhi') == 0


def test_count_hi_2_4():
    assert count_hi_2('hixhi') == 1


def test_count_hi_2_5():
    assert count_hi_2('hixhhi') == 2


def test_count_hi_2_6():
    assert count_hi_2('hihihi') == 3


def test_count_hi_2_7():
    assert count_hi_2('hihihix') == 3


def test_count_hi_2_8():
    assert count_hi_2('xhihihix') == 2


def test_count_hi_2_9():
    assert count_hi_2('xxhi') == 0


def test_count_hi_2_10():
    assert count_hi_2('hixxhi') == 1


def test_count_hi_2_11():
    assert count_hi_2('hi') == 1


def test_count_hi_2_12():
    assert count_hi_2('xxxx') == 0


def test_count_hi_2_13():
    assert count_hi_2('h') == 0


def test_count_hi_2_14():
    assert count_hi_2('x') == 0


def test_count_hi_2_15():
    assert count_hi_2('') == 0


def test_count_hi_2_16():
    assert count_hi_2('Hellohi') == 1
```
