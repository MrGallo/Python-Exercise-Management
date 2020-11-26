# string_e




Return true if the given string contains between 1 and 3 'e' chars.

```
string_e("Hello") → true
string_e("Heelle") → true
string_e("Heelele") → false
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p173784) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def string_e(string: str) -> bool:
    pass


result = string_e('Hello')
print(result)
```

## Tests
```python
from main import string_e


def test_string_e_1():
    assert string_e('Hello') == True


def test_string_e_2():
    assert string_e('Heelle') == True


def test_string_e_3():
    assert string_e('Heelele') == False


def test_string_e_4():
    assert string_e('Hll') == False


def test_string_e_5():
    assert string_e('e') == True


def test_string_e_6():
    assert string_e('') == False
```
