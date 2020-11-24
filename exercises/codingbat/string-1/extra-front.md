# extra_front
**Topic:** 



Given a string, return a new string made of 3 copies of the first 2 chars of the original string. The string may be any length. If there are fewer than 2 chars, use whatever is there.

<code>
extra_front("Hello") → "HeHeHe"
extra_front("ab") → "ababab"
extra_front("H") → "HHH"
</code>

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p172063) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def extra_front(str: str) -> str:
```

## Tests
```python
from main import extra_front


def test_extra_front_1():
    assert extra_front('Hello') == 'HeHeHe'


def test_extra_front_2():
    assert extra_front('ab') == 'ababab'


def test_extra_front_3():
    assert extra_front('H') == 'HHH'


def test_extra_front_4():
    assert extra_front('') == ''


def test_extra_front_5():
    assert extra_front('Candy') == 'CaCaCa'


def test_extra_front_6():
    assert extra_front('Code') == 'CoCoCo'
```
