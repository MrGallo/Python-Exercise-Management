# fizz_array_2





Given a number n, create and return a new string list of length n, containing the strings "0", "1" "2" .. through n-1. N may be 0, in which case just return a length 0 list. Note: String.valueOf(xxx) will make the String form of most types. The syntax to make a new string list is: new String[desired_length] &nbsp;(See also: <a href=/doc/practice/fizzbuzz-code.html>FizzBuzz Code</a>)

```
fizzList2(4) -> ["0", "1", "2", "3"]
fizzList2(10) -> ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
fizzList2(2) -> ["0", "1"]
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p178353) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def fizz_array_2(n: int) -> List[str]:
    pass


result = fizz_array_2(4)
print(result)
```

## Tests
```python
from main import fizz_array_2


def test_fizz_array_2_1():
    assert fizz_array_2(4) == ['0', '1', '2', '3']


def test_fizz_array_2_2():
    assert fizz_array_2(10) == ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def test_fizz_array_2_3():
    assert fizz_array_2(2) == ['0', '1']


def test_fizz_array_2_4():
    assert fizz_array_2(1) == ['0']


def test_fizz_array_2_5():
    assert fizz_array_2(0) == []


def test_fizz_array_2_6():
    assert fizz_array_2(7) == ['0', '1', '2', '3', '4', '5', '6']


def test_fizz_array_2_7():
    assert fizz_array_2(9) == ['0', '1', '2', '3', '4', '5', '6', '7', '8']


def test_fizz_array_2_8():
    assert fizz_array_2(11) == ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
```
