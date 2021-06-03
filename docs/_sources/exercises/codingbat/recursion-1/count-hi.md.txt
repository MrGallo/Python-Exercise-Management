# count_hi





Given a string, compute recursively (no loops) the number of times lowercase `"hi"` appears in the string.

```
count_hi("xxhixx") -> 1
count_hi("xhixhix") -> 2
count_hi("hi") -> 1
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p184029) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def count_hi(string: str) -> int:
    pass


result = count_hi('xxhixx')
print(result)
```

## Tests
```python
from main import count_hi


def test_count_hi_1():
    assert count_hi('xxhixx') == 1


def test_count_hi_2():
    assert count_hi('xhixhix') == 2


def test_count_hi_3():
    assert count_hi('hi') == 1


def test_count_hi_4():
    assert count_hi('hihih') == 2


def test_count_hi_5():
    assert count_hi('h') == 0


def test_count_hi_6():
    assert count_hi('') == 0


def test_count_hi_7():
    assert count_hi('ihihihihih') == 4


def test_count_hi_8():
    assert count_hi('ihihihihihi') == 5


def test_count_hi_9():
    assert count_hi('hiAAhi12hi') == 3


def test_count_hi_10():
    assert count_hi('xhixhxihihhhih') == 3


def test_count_hi_11():
    assert count_hi('ship') == 1
```
