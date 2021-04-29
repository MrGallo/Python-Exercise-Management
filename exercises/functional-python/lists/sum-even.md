# Sum Even



**Requirements:**
```eval_rst
- :ref:`fundamentals:loop with an accumulator variable`
- :ref:`fundamentals:loop through a list (for)`
- :ref:`fundamentals:if, else`
- :ref:`fundamentals:returning a value`

```


See starter code docstring for requirements.

## Starter Code
```python
from typing import List


def sum_even(numbers: List[int]) -> int:
    """Returns the sum all even numbers in a list.

    Args:
        numbers: A list of integers.
    Returns:
        The sum of the even integers.
    
    Note: Use modulus (%) to discover even integers.
    """
    return 0
```

## Tests
```python
from main import sum_even


def test_sum_even():
    assert sum_even([1, 1, 1, 2]) == 2
    assert sum_even([2, 1, 1, 2]) == 4
    assert sum_even([4, 1, 1, 21]) == 4
    assert sum_even([]) == 0
    assert sum_even([1, 3, 5, 7, 9]) == 0
    assert sum_even([-2]) == -2
```
