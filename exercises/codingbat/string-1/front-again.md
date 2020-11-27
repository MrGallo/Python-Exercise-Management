# front_again





Given a string, return true if the first 2 chars in the string also appear at the end of the string, such as with "edited".

```
front_again("edited") â†’ true
front_again("edit") â†’ false
front_again("ed") â†’ true
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p196652) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def front_again(string: str) -> bool:
    pass


result = front_again('edited')
print(result)
```

## Tests
```python
from main import front_again


def test_front_again_1():
    assert front_again('edited') == True


def test_front_again_2():
    assert front_again('edit') == False


def test_front_again_3():
    assert front_again('ed') == True


def test_front_again_4():
    assert front_again('jj') == True


def test_front_again_5():
    assert front_again('jjj') == True


def test_front_again_6():
    assert front_again('jjjj') == True


def test_front_again_7():
    assert front_again('jjjk') == False


def test_front_again_8():
    assert front_again('x') == False


def test_front_again_9():
    assert front_again('') == False


def test_front_again_10():
    assert front_again('java') == False


def test_front_again_11():
    assert front_again('javaja') == True
```
