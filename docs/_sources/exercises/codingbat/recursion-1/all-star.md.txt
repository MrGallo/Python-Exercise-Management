# all_star





Given a string, compute recursively a new string where all the adjacent chars are now separated by a "*".

```
all_star("hello") -> "h*e*l*l*o"
all_star("abc") -> "a*b*c"
all_star("ab") -> "a*b"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p183394) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def all_star(string: str) -> str:
    pass


result = all_star('hello')
print(result)
```

## Tests
```python
from main import all_star


def test_all_star_1():
    assert all_star('hello') == 'h*e*l*l*o'


def test_all_star_2():
    assert all_star('abc') == 'a*b*c'


def test_all_star_3():
    assert all_star('ab') == 'a*b'


def test_all_star_4():
    assert all_star('a') == 'a'


def test_all_star_5():
    assert all_star('') == ''


def test_all_star_6():
    assert all_star('3.14') == '3*.*1*4'


def test_all_star_7():
    assert all_star('Chocolate') == 'C*h*o*c*o*l*a*t*e'


def test_all_star_8():
    assert all_star('1234') == '1*2*3*4'
```
