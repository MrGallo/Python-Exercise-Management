# fizz_array_3





Given <b>start</b> and <b>end</b> numbers, return a new list containing the sequence of integers from start up to but not including end, so start=5 and end=10 yields {5, 6, 7, 8, 9}. The end number will be greater or equal to the start number. Note that a length-0 list is valid. (See also: <a href=/doc/practice/fizzbuzz-code.html>FizzBuzz Code</a>)

```
fizzList3(5, 10) -> [5, 6, 7, 8, 9]
fizzList3(11, 18) -> [11, 12, 13, 14, 15, 16, 17]
fizzList3(1, 3) -> [1, 2]
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p142539) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def fizz_array_3(start: int, end: int) -> List[int]:
    pass


result = fizz_array_3(5, 10)
print(result)
```

## Tests
```python
from main import fizz_array_3


def test_fizz_array_3_1():
    assert fizz_array_3(5, 10) == [5, 6, 7, 8, 9]


def test_fizz_array_3_2():
    assert fizz_array_3(11, 18) == [11, 12, 13, 14, 15, 16, 17]


def test_fizz_array_3_3():
    assert fizz_array_3(1, 3) == [1, 2]


def test_fizz_array_3_4():
    assert fizz_array_3(1, 2) == [1]


def test_fizz_array_3_5():
    assert fizz_array_3(1, 1) == []


def test_fizz_array_3_6():
    assert fizz_array_3(1000, 1005) == [1000, 1001, 1002, 1003, 1004]
```
