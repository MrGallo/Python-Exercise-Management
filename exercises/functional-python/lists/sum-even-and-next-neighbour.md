# Sum even and next neighbour





Requirements are in the starter code docstring.

## Starter Code
```python
from typing import List


def sum_even_and_next_neighbour(numbers: List[int]) -> int:
    """Returns the sum all even numbers and their next neighbour.

    Args:
        numbers: A list of integers.
    Returns:
        The sum of the even integers, including next neighbours of even numbers.
    
    Note: A next neighbour is an integer that appears after an integer in the list.
          These numbers will be included in the total. Do not count even numbers twice.

          e.g., [1, 2, 3, 4, 6, 7, 9, 11, 12]
          In the example list, we need to include 3 into the total because it is
          2's next neighbour. Same with 7 (6's next neighbour). 
          We also should not include 6 into the total twice.
          The total for this list would be: 2 + 3 + 4 + 6 + 7 + 12 = 34
    """
    return 0
```

## Tests
```python
from main import sum_even_and_next_neighbour


def test_sum_even_and_next_neighbour():
    assert sum_even_and_next_neighbour([]) == 0
    assert sum_even_and_next_neighbour([2, 2, 2]) == 6
    assert sum_even_and_next_neighbour([1, 2, 3, 4]) == 9
    assert sum_even_and_next_neighbour([2, 1, 2, 1]) == 6
    assert sum_even_and_next_neighbour([1, 1, 1, 1]) == 0
    assert sum_even_and_next_neighbour([2, 99]) == 101
```
