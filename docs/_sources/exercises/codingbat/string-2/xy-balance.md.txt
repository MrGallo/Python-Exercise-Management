# xy_balance





We'll say that a String is xy-balanced if for all the 'x' chars in the string, there exists a 'y' char somewhere later in the string. So "xxy" is balanced, but "xyx" is not. One 'y' can balance multiple 'x's. Return true if the given string is xy-balanced.

```
xy_balance("aaxbby") â†’ true
xy_balance("aaxbb") â†’ false
xy_balance("yaaxbb") â†’ false
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p134250) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def xy_balance(string: str) -> bool:
    pass


result = xy_balance('aaxbby')
print(result)
```

## Tests
```python
from main import xy_balance


def test_xy_balance_1():
    assert xy_balance('aaxbby') == True


def test_xy_balance_2():
    assert xy_balance('aaxbb') == False


def test_xy_balance_3():
    assert xy_balance('yaaxbb') == False


def test_xy_balance_4():
    assert xy_balance('yaaxbby') == True


def test_xy_balance_5():
    assert xy_balance('xaxxbby') == True


def test_xy_balance_6():
    assert xy_balance('xaxxbbyx') == False


def test_xy_balance_7():
    assert xy_balance('xxbxy') == True


def test_xy_balance_8():
    assert xy_balance('xxbx') == False


def test_xy_balance_9():
    assert xy_balance('bbb') == True


def test_xy_balance_10():
    assert xy_balance('bxbb') == False


def test_xy_balance_11():
    assert xy_balance('bxyb') == True


def test_xy_balance_12():
    assert xy_balance('xy') == True


def test_xy_balance_13():
    assert xy_balance('y') == True


def test_xy_balance_14():
    assert xy_balance('x') == False


def test_xy_balance_15():
    assert xy_balance('') == True


def test_xy_balance_16():
    assert xy_balance('yxyxyxyx') == False


def test_xy_balance_17():
    assert xy_balance('yxyxyxyxy') == True


def test_xy_balance_18():
    assert xy_balance('12xabxxydxyxyzz') == True
```
