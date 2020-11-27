# repeat_front





Given a string and an int n, return a string made of the first n characters of the string, followed by the first n-1 characters of the string, and so on. You may assume that n is between 0 and the length of the string, inclusive (i.e. n &gt;= 0 and n &lt;= str.length()).

```
repeat_front("Chocolate", 4) → "ChocChoChC"
repeat_front("Chocolate", 3) → "ChoChC"
repeat_front("Ice Cream", 2) → "IcI"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p128796) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def repeat_front(string: str, n: int) -> str:
    pass


result = repeat_front('Chocolate', 4)
print(result)
```

## Tests
```python
from main import repeat_front


def test_repeat_front_1():
    assert repeat_front('Chocolate', 4) == 'ChocChoChC'


def test_repeat_front_2():
    assert repeat_front('Chocolate', 3) == 'ChoChC'


def test_repeat_front_3():
    assert repeat_front('Ice Cream', 2) == 'IcI'


def test_repeat_front_4():
    assert repeat_front('Ice Cream', 1) == 'I'


def test_repeat_front_5():
    assert repeat_front('Ice Cream', 0) == ''


def test_repeat_front_6():
    assert repeat_front('xyz', 3) == 'xyzxyx'


def test_repeat_front_7():
    assert repeat_front('', 0) == ''


def test_repeat_front_8():
    assert repeat_front('Java', 4) == 'JavaJavJaJ'


def test_repeat_front_9():
    assert repeat_front('Java', 1) == 'J'
```
