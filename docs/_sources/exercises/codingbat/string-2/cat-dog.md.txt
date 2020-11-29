# cat_dog



**Requirements:**
```eval_rst
- :ref:`fundamentals:substrings and slicing`
- :ref:`fundamentals:if, elif, else`
- :ref:`fundamentals:loop through a string (while)`
- :ref:`fundamentals:loop with an accumulator variable`

```


Return true if the string "cat" and "dog" appear the same number of times in the given string.

```
cat_dog("catdog") -> true
cat_dog("catcat") -> false
cat_dog("1cat1cadodog") -> true
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p111624) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def cat_dog(string: str) -> bool:
    pass


result = cat_dog('catdog')
print(result)
```

## Tests
```python
from main import cat_dog


def test_cat_dog_1():
    assert cat_dog('catdog') == True


def test_cat_dog_2():
    assert cat_dog('catcat') == False


def test_cat_dog_3():
    assert cat_dog('1cat1cadodog') == True


def test_cat_dog_4():
    assert cat_dog('catxxdogxxxdog') == False


def test_cat_dog_5():
    assert cat_dog('catxdogxdogxcat') == True


def test_cat_dog_6():
    assert cat_dog('catxdogxdogxca') == False


def test_cat_dog_7():
    assert cat_dog('dogdogcat') == False


def test_cat_dog_8():
    assert cat_dog('dogogcat') == True


def test_cat_dog_9():
    assert cat_dog('dog') == False


def test_cat_dog_10():
    assert cat_dog('cat') == False


def test_cat_dog_11():
    assert cat_dog('ca') == True


def test_cat_dog_12():
    assert cat_dog('c') == True


def test_cat_dog_13():
    assert cat_dog('') == True
```
