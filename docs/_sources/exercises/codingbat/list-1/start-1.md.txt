# start_1





Start with 2 int lists, a and b, of any length. Return how many of the lists have 1 as their first element.

```
start_1([1, 2, 3], [1, 3]) -> 2
start_1([7, 2, 3], [1]) -> 1
start_1([1, 2], []) -> 1
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p109660) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
from typing import List


def start_1(a: List[int], b: List[int]) -> int:
    pass


result = start_1([1, 2, 3], [1, 3])
print(result)
```

## Tests
```python
from main import start_1


def test_start_1_1():
    assert start_1([1, 2, 3], [1, 3]) == 2


def test_start_1_2():
    assert start_1([7, 2, 3], [1]) == 1


def test_start_1_3():
    assert start_1([1, 2], []) == 1


def test_start_1_4():
    assert start_1([], [1, 2]) == 1


def test_start_1_5():
    assert start_1([7], []) == 0


def test_start_1_6():
    assert start_1([7], [1]) == 1


def test_start_1_7():
    assert start_1([1], [1]) == 2


def test_start_1_8():
    assert start_1([7], [8]) == 0


def test_start_1_9():
    assert start_1([], []) == 0


def test_start_1_10():
    assert start_1([1, 3], [1]) == 2
```
