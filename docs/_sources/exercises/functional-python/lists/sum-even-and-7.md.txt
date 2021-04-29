# Sum even and 7



**Requirements:**
```eval_rst
- :ref:`fundamentals:mathematical operations`
- :ref:`fundamentals:if, else`
- :ref:`fundamentals:loop with an accumulator variable`
- :ref:`fundamentals:loop through a list (for)`
- :ref:`fundamentals:returning a value`

```


See starter code docstring for requirements.

## Starter Code
```python
from typing import List


def sum_even_and_7(numbers: List[int]) -> int:
    """Returns the sum all even numbers, and 7's, in a list.

    Args:
        numbers: A list of integers.
    Returns:
        The sum of the even integers, including all 7's.
    
    Note: Use modulus (%) to discover even integers.
    """
    return 0
```

## Tests
```python
from main import sum_even_and_7


def test_sum_even_and_7():
    assert sum_even_and_7([1, 2, 3, 4]) == 6
    assert sum_even_and_7([7, 1, 2]) == 9
    assert sum_even_and_7([5, 7, 9]) == 7
    assert sum_even_and_7([1, 1, 1, -1]) == 0
```
