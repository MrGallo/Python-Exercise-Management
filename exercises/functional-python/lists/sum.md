# sum



**Requirements:**
```eval_rst
- :ref:`fundamentals:loop with an accumulator variable`
- :ref:`fundamentals:loop through a list (for)`
- :ref:`fundamentals:returning a value`

```


Please see starter code docstring for requirements.

## Starter Code
```python
from typing import List


def sum_list(numbers: List[float]) -> float:
    """Returns the sum of a list of numbers.

    Args:
        numbers: A list of float numbers.
    Returns:
        The sum of the numbers.
    
    Note: Do NOT use the sum() built-in function to 
          accomplish this. Use a loop.
    """
    return 0
```

## Tests
```python
from main import sum_list


def test_sum_list():
    assert sum_list([1.0, 1.0, 1.0]) == 3.0
    assert sum_list([1.5, 1.5, 1.5]) == 4.5
    assert sum_list([]) == 0
    assert sum_list([-10, 10]) == 0
```
