# str_copies





Given a string and a non-empty substring <b>sub</b>, compute recursively if at least n copies of sub appear in the string somewhere, possibly with overlapping. N will be non-negative.

```
str_copies("catcowcat", "cat", 2) -> true
str_copies("catcowcat", "cow", 2) -> false
str_copies("catcowcat", "cow", 1) -> true
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p118182) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def str_copies(string: str, sub: str, n: int) -> bool:
    pass


result = str_copies('catcowcat', 'cat', 2)
print(result)
```

## Tests
```python
from main import str_copies


def test_str_copies_1():
    assert str_copies('catcowcat', 'cat', 2) == True


def test_str_copies_2():
    assert str_copies('catcowcat', 'cow', 2) == False


def test_str_copies_3():
    assert str_copies('catcowcat', 'cow', 1) == True


def test_str_copies_4():
    assert str_copies('iiijjj', 'i', 3) == True


def test_str_copies_5():
    assert str_copies('iiijjj', 'i', 4) == False


def test_str_copies_6():
    assert str_copies('iiijjj', 'ii', 2) == True


def test_str_copies_7():
    assert str_copies('iiijjj', 'ii', 3) == False


def test_str_copies_8():
    assert str_copies('iiijjj', 'x', 3) == False


def test_str_copies_9():
    assert str_copies('iiijjj', 'x', 0) == True


def test_str_copies_10():
    assert str_copies('iiiiij', 'iii', 3) == True


def test_str_copies_11():
    assert str_copies('iiiiij', 'iii', 4) == False


def test_str_copies_12():
    assert str_copies('ijiiiiij', 'iiii', 2) == True


def test_str_copies_13():
    assert str_copies('ijiiiiij', 'iiii', 3) == False


def test_str_copies_14():
    assert str_copies('dogcatdogcat', 'dog', 2) == True
```
