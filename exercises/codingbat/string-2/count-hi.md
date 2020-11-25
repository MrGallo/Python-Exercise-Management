# count_hi




Return the number of times that the string "hi" appears anywhere in the given string.

```
count_hi("abc hi ho") → 1
count_hi("ABChi hi") → 2
count_hi("hihi") → 2
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p147448) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def count_hi(string: str) -> int:
    pass


result = count_hi('abc hi ho')
print(result)
```

## Tests
```python
from main import count_hi


def test_count_hi_1():
    assert count_hi('abc hi ho') == 1


def test_count_hi_2():
    assert count_hi('ABChi hi') == 2


def test_count_hi_3():
    assert count_hi('hihi') == 2


def test_count_hi_4():
    assert count_hi('hiHIhi') == 2


def test_count_hi_5():
    assert count_hi('') == 0


def test_count_hi_6():
    assert count_hi('h') == 0


def test_count_hi_7():
    assert count_hi('hi') == 1


def test_count_hi_8():
    assert count_hi('Hi is no HI on ahI') == 0


def test_count_hi_9():
    assert count_hi('hiho not HOHIhi') == 2
```
