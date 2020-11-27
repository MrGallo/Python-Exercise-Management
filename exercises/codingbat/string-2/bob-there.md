# bob_there





Return true if the given string contains a "bob" string, but where the middle 'o' char can be any char.

```
bob_there("abcbob") â†’ true
bob_there("b9b") â†’ true
bob_there("bac") â†’ false
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p175762) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def bob_there(string: str) -> bool:
    pass


result = bob_there('abcbob')
print(result)
```

## Tests
```python
from main import bob_there


def test_bob_there_1():
    assert bob_there('abcbob') == True


def test_bob_there_2():
    assert bob_there('b9b') == True


def test_bob_there_3():
    assert bob_there('bac') == False


def test_bob_there_4():
    assert bob_there('bbb') == True


def test_bob_there_5():
    assert bob_there('abcdefb') == False


def test_bob_there_6():
    assert bob_there('123abcbcdbabxyz') == True


def test_bob_there_7():
    assert bob_there('b12') == False


def test_bob_there_8():
    assert bob_there('b1b') == True


def test_bob_there_9():
    assert bob_there('b12b1b') == True


def test_bob_there_10():
    assert bob_there('bbc') == False


def test_bob_there_11():
    assert bob_there('bbb') == True


def test_bob_there_12():
    assert bob_there('bb') == False


def test_bob_there_13():
    assert bob_there('b') == False
```
