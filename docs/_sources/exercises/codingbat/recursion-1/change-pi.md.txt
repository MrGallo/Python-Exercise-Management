# change_pi





Given a string, compute recursively (no loops) a new string where all appearances of "pi" have been replaced by `"3.14"`.

```
change_pi("xpix") -> "x3.14x"
change_pi("pipi") -> "3.143.14"
change_pi("pip") -> "3.14p"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p170924) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def change_pi(string: str) -> str:
    pass


result = change_pi('xpix')
print(result)
```

## Tests
```python
from main import change_pi


def test_change_pi_1():
    assert change_pi('xpix') == 'x3.14x'


def test_change_pi_2():
    assert change_pi('pipi') == '3.143.14'


def test_change_pi_3():
    assert change_pi('pip') == '3.14p'


def test_change_pi_4():
    assert change_pi('pi') == '3.14'


def test_change_pi_5():
    assert change_pi('hip') == 'hip'


def test_change_pi_6():
    assert change_pi('p') == 'p'


def test_change_pi_7():
    assert change_pi('x') == 'x'


def test_change_pi_8():
    assert change_pi('') == ''


def test_change_pi_9():
    assert change_pi('pixx') == '3.14xx'


def test_change_pi_10():
    assert change_pi('xyzzy') == 'xyzzy'


def test_change_pi_11():
    assert change_pi('Pixx') == 'Pixx'


def test_change_pi_12():
    assert change_pi('pIxx') == 'pIxx'


def test_change_pi_13():
    assert change_pi('PIxx') == 'PIxx'
```
