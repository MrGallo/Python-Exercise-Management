# middle_three




Given a string of odd length, return the string length 3 from its middle, so "Candy" yields "and". The string length will be at least 3.

```
middle_three("Candy") → "and"
middle_three("and") → "and"
middle_three("solving") → "lvi"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p115863) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def middle_three(string: str) -> str:
    pass


result = middle_three('Candy')
print(result)
```

## Tests
```python
from main import middle_three


def test_middle_three_1():
    assert middle_three('Candy') == 'and'


def test_middle_three_2():
    assert middle_three('and') == 'and'


def test_middle_three_3():
    assert middle_three('solving') == 'lvi'


def test_middle_three_4():
    assert middle_three('Hi yet Hi') == 'yet'


def test_middle_three_5():
    assert middle_three('java yet java') == 'yet'


def test_middle_three_6():
    assert middle_three('Chocolate') == 'col'


def test_middle_three_7():
    assert middle_three('XabcxyzabcX') == 'xyz'
```
