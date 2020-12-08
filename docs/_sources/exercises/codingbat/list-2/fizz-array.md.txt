# fizz_array





Given a number n, create and return a new int list of length n, containing the numbers 0, 1, 2, ... n-1. The given n may be 0, in which case just return a length 0 list. You do not need a separate if-statement for the length-0 case; the for-loop should naturally execute 0 times in that case, so it just works. The syntax to make a new int list is: new int[desired_length]  &nbsp; (See also: <a href=/doc/practice/fizzbuzz-code.html>FizzBuzz Code</a>)

```
fizzList(4) -> [0, 1, 2, 3]
fizzList(1) -> [0]
fizzList(10) -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p180920) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def fizz_array(n: int) -> List[int]:
    pass


result = fizz_array(4)
print(result)
```

## Tests
```python
from main import fizz_array


def test_fizz_array_1():
    assert fizz_array(4) == [0, 1, 2, 3]


def test_fizz_array_2():
    assert fizz_array(1) == [0]


def test_fizz_array_3():
    assert fizz_array(10) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_fizz_array_4():
    assert fizz_array(0) == []


def test_fizz_array_5():
    assert fizz_array(2) == [0, 1]


def test_fizz_array_6():
    assert fizz_array(7) == [0, 1, 2, 3, 4, 5, 6]
```
