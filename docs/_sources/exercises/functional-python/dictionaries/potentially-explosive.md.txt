# Potentially Explosive



**Requirements:**
```eval_rst
- :ref:`fundamentals:iterating through dictionary keys`
- :ref:`fundamentals:if, else`
- :ref:`fundamentals:returning a value`

```


An inventory is considered "potentially explosive" if it contains
even the mention of both "fire" and "propane" in the dictionary's keys.
The quantities of each element are irrevelant.

### Hint

Use `dict.keys()` for a list of the dictionary's keys. e.g.,

```python
some_dict = {"first_name": "Jeff"}
"first_name" in some_dict.keys()  # True
"age" in some_dict.keys()  # False
"name" in some_dict.keys()  # False
```

## Starter Code
```python
from typing import Dict


def is_potentially_explosive(inventory: Dict) -> bool:
    """Determines if your inventory is potentially explosive.
    
    An inventory is considered potentially explosive if it contains
    even the mention of both "fire" and "propane" in the dictionary's keys.
    The quantities of each element are irrevelant.
    
    Args:
        inventory: A dictionary that may be explosive.
    Returns:
        True if potentially explosive, False otherwise.
    """
    return None
```

## Tests
```python
from main import is_potentially_explosive


def test_no_mention_of_either_item():
    inventory = {
        "apples": 4,
        "oranges": 5
    }

    assert is_potentially_explosive(inventory) is False


def test_only_propane_not_explosive():
    inventory = {
        "apples": 4,
        "propane": 5
    }

    assert is_potentially_explosive(inventory) is False


def test_only_fire_not_explosive():
    inventory = {
        "apples": 4,
        "fire": 5
    }

    assert is_potentially_explosive(inventory) is False


def test_both_fire_and_propane_is_potentially_explosive():
    inventory = {
        "propane": 4,
        "fire": 5
    }
    assert is_potentially_explosive(inventory) is True


def test_also_potentially_explosive_if_quantity_is_0():
    inventory = {
        "propane": 0,
        "fire": 0
    }
    assert is_potentially_explosive(inventory) is True
```
