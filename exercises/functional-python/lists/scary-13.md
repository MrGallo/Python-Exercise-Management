# Scary 13





Requirements are in the starter code docstring.

## Starter Code
```python
from typing import List


def sum_scary_13(numbers: List[int]) -> int:
    """Returns the sum all numbers jumping over 13 and the next number.

    Args:
        numbers: A list of integers.
    Returns:
        The sum of all numbers, not including 13 and it's next neighbour.
    
    Note: A next neighbour is an integer that appears after an integer in the list.
          Your program is afraid of the number 13, so it will add neither that number
          nor the one next in the list to the toal.

          E.g. 1, [5, 6, 13, 1, 7]
          Will add 5 + 6 + 7 = 18

          E.g. 2, [5, 6, 13, 13, 1, 7]
          In this case, the program doesn't even notice the second 13 because
          it jumped over because of the first 13.
          The program will add 5 + 6 + 1 + 7 = 19
    """
    return 0
```

## Tests
```python
from main import sum_scary_13


def test_example_1():
    assert sum_scary_13([5, 6, 13, 1, 7]) == 18


def test_example_2():
    assert sum_scary_13([5, 6, 13, 13, 1, 7]) == 19


def test_sum_scary_13():
    assert sum_scary_13([]) == 0
    assert sum_scary_13([13]) == 0
    assert sum_scary_13([1, 2, 3]) == 6
    assert sum_scary_13([0, 13, 99]) == 0
    assert sum_scary_13([1, 2, 13, 3]) == 3
```
