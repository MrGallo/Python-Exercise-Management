# Calculating remaining attempts



**Requirements:**
```eval_rst
- :ref:`fundamentals:mathematical operations`
- :ref:`fundamentals:returning a value`
- :ref:`fundamentals:docstrings`

```


Complete the starter code. Details about how the function works are in the docstring. *Hint: Use `len(list)` to check how many items are in a list.*

## Starter Code
```python
def calc_attempts_remaining(attempts_allowed: int, incorrect: List[str]) -> int:
    """Determine the number of guesses remaining.

    Based on the initial number of allowed attempts and the number
    of incorrect guesses.
    
    Args:
        attempts_allowed: The number of total allowed guesses.
        incorrect: A list containing all the incorrect guesses.
    
    Returns:
        How many remaining guesses the player has.
    """
    pass
```

## Tests
```python
from main import calc_attempts_remaining


def test_calc_attempts_remaining():
    assert calc_attempts_remaining(5, []) == 5
    assert calc_attempts_remaining(5, ['a']) == 4
    assert calc_attempts_remaining(5, list('12345')) == 0
```
