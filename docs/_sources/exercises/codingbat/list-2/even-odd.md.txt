# even_odd





Return an list that contains the exact same numbers as the given list, but rearranged so that all the even numbers come before all the odd numbers. Other than that, the numbers can be in any order. You may modify and return the given list, or make a new list.

```
even_odd([1, 0, 1, 0, 0, 1, 1]) -> [0, 0, 0, 1, 1, 1, 1]
even_odd([3, 3, 2]) -> [2, 3, 3]
even_odd([2, 2, 2]) -> [2, 2, 2]
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p105771) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def even_odd(nums: List[int]) -> List[int]:
    pass


result = even_odd([1, 0, 1, 0, 0, 1, 1])
print(result)
```

## Tests
```python
from main import even_odd


def test_even_odd_1():
    assert even_odd([1, 0, 1, 0, 0, 1, 1]) == [0, 0, 0, 1, 1, 1, 1]


def test_even_odd_2():
    assert even_odd([3, 3, 2]) == [2, 3, 3]


def test_even_odd_3():
    assert even_odd([2, 2, 2]) == [2, 2, 2]


def test_even_odd_4():
    assert even_odd([3, 2, 2]) == [2, 2, 3]


def test_even_odd_5():
    assert even_odd([1, 1, 0, 1, 0]) == [0, 0, 1, 1, 1]


def test_even_odd_6():
    assert even_odd([1]) == [1]


def test_even_odd_7():
    assert even_odd([1, 2]) == [2, 1]


def test_even_odd_8():
    assert even_odd([2, 1]) == [2, 1]


def test_even_odd_9():
    assert even_odd([]) == []
```
