# ends_ly





Given a string, return true if it ends in "ly".

```
ends_ly("oddly") → true
ends_ly("y") → false
ends_ly("oddy") → false
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p103895) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def ends_ly(string: str) -> bool:
    pass


result = ends_ly('oddly')
print(result)
```

## Tests
```python
from main import ends_ly


def test_ends_ly_1():
    assert ends_ly('oddly') == True


def test_ends_ly_2():
    assert ends_ly('y') == False


def test_ends_ly_3():
    assert ends_ly('oddy') == False


def test_ends_ly_4():
    assert ends_ly('oddl') == False


def test_ends_ly_5():
    assert ends_ly('olydd') == False


def test_ends_ly_6():
    assert ends_ly('ly') == True


def test_ends_ly_7():
    assert ends_ly('') == False


def test_ends_ly_8():
    assert ends_ly('falsey') == False


def test_ends_ly_9():
    assert ends_ly('evenly') == True
```
