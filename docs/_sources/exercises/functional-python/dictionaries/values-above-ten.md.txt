# Values Above Ten



**Requirements:**
```eval_rst
- :ref:`fundamentals:iterating through dictionary values`
- :ref:`fundamentals:list building and filtering`
- :ref:`fundamentals:returning a value`

```


See starter code docstring.

## Starter Code
```python
from typing import Dict, List


def values_above_10(inventory: Dict[str, int]) -> List:
    """Gives a list of dictionary values greater than 10.
    
    Args:
        inventory: Dictionary of inventory-like key value pairs.
    Returns:
        List of values (not keys) from the dictionary above 10.

    """
    return None
```

## Tests
```python
from main import values_above_10


def test_values_above_10_empty():
    inventory = {}
    assert values_above_10(inventory) == []


def test_values_above_10_doesnt_include_10():
    inventory = {"a": 0, "b": 10}
    assert values_above_10(inventory) == []


def test_values_above_10():
    inventory = {"a": 0, "b": 10, "c": 11, "d": -10}
    assert values_above_10(inventory) == [11]

    inventory = {"a": 55, "b": 11, "c": 11, "d": 23}
    assert values_above_10(inventory) == [55, 11, 11, 23]

    inventory = {"d": 55, "c": 11, "b": 11, "a": 23}
    assert values_above_10(inventory) == [55, 11, 11, 23]
```
