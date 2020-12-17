# fizz_buzz





This is slightly more difficult version of the famous FizzBuzz problem which is sometimes given as a first problem for job interviews. Consider the series of numbers beginning at `start` and running up to but not including `end`, so for example `start=1` and `end=5` gives the series `1, 2, 3, 4`. Return a string list containing the string form of these numbers, except for multiples of `3`, use `"Fizz"` instead of the number, for multiples of `5` use `"Buzz"`, and for multiples of both `3` and `5` use "FizzBuzz". In Python, the `str()` function will convert a value to a string. This version is a little more complicated than the usual version since you have to append to a list instead of just printing, and we vary the start/end instead of just always doing `1..100`.

```
fizz_buzz(1, 6) -> ["1", "2", "Fizz", "4", "Buzz"]
fizz_buzz(1, 8) -> ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7"]
fizz_buzz(1, 11) -> ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz"]
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p153059) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def fizz_buzz(start: int, end: int) -> List[str]:
    pass


result = fizz_buzz(1, 6)
print(result)
```

## Tests
```python
from main import fizz_buzz


def test_fizz_buzz_1():
    assert fizz_buzz(1, 6) == ['1', '2', 'Fizz', '4', 'Buzz']


def test_fizz_buzz_2():
    assert fizz_buzz(1, 8) == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7']


def test_fizz_buzz_3():
    assert fizz_buzz(1, 11) == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz']


def test_fizz_buzz_4():
    assert fizz_buzz(1, 16) == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']


def test_fizz_buzz_5():
    assert fizz_buzz(1, 4) == ['1', '2', 'Fizz']


def test_fizz_buzz_6():
    assert fizz_buzz(1, 2) == ['1']


def test_fizz_buzz_7():
    assert fizz_buzz(50, 56) == ['Buzz', 'Fizz', '52', '53', 'Fizz', 'Buzz']


def test_fizz_buzz_8():
    assert fizz_buzz(15, 17) == ['FizzBuzz', '16']


def test_fizz_buzz_9():
    assert fizz_buzz(30, 36) == ['FizzBuzz', '31', '32', 'Fizz', '34', 'Buzz']


def test_fizz_buzz_10():
    assert fizz_buzz(1000, 1006) == ['Buzz', '1001', 'Fizz', '1003', '1004', 'FizzBuzz']


def test_fizz_buzz_11():
    assert fizz_buzz(99, 102) == ['Fizz', 'Buzz', '101']


def test_fizz_buzz_12():
    assert fizz_buzz(14, 20) == ['14', 'FizzBuzz', '16', '17', 'Fizz', '19']
```
