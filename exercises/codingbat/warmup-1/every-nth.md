# every_nth





Given a non-empty string and an int N, return the string made starting with char 0, and then every Nth char of the string. So if N is 3, use char 0, 3, 6, ... and so on. N is 1 or more.

```
every_nth("Miracle", 2) â†’ "Mrce"
every_nth("abcdefg", 2) â†’ "aceg"
every_nth("abcdefg", 3) â†’ "adg"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p196441) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def every_nth(string: str, n: int) -> str:
    pass


result = every_nth('Miracle', 2)
print(result)
```

## Tests
```python
from main import every_nth


def test_every_nth_1():
    assert every_nth('Miracle', 2) == 'Mrce'


def test_every_nth_2():
    assert every_nth('abcdefg', 2) == 'aceg'


def test_every_nth_3():
    assert every_nth('abcdefg', 3) == 'adg'


def test_every_nth_4():
    assert every_nth('Chocolate', 3) == 'Cca'


def test_every_nth_5():
    assert every_nth('Chocolates', 3) == 'Ccas'


def test_every_nth_6():
    assert every_nth('Chocolates', 4) == 'Coe'


def test_every_nth_7():
    assert every_nth('Chocolates', 100) == 'C'
```
