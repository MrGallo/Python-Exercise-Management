# see_color
**Topic:** 



Given a string, if the string begins with "red" or "blue" return that color string, otherwise return the empty string.

```
see_color("redxx") → "red"
see_color("xxred") → ""
see_color("blueTimes") → "blue"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p199216) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def see_color(str: str) -> str:
```

## Tests
```python
from main import see_color


def test_see_color_1():
    assert see_color('redxx') == 'red'


def test_see_color_2():
    assert see_color('xxred') == ''


def test_see_color_3():
    assert see_color('blueTimes') == 'blue'


def test_see_color_4():
    assert see_color('NoColor') == ''


def test_see_color_5():
    assert see_color('red') == 'red'


def test_see_color_6():
    assert see_color('re') == ''


def test_see_color_7():
    assert see_color('blu') == ''


def test_see_color_8():
    assert see_color('blue') == 'blue'


def test_see_color_9():
    assert see_color('a') == ''


def test_see_color_10():
    assert see_color('') == ''


def test_see_color_11():
    assert see_color('xyzred') == ''
```
