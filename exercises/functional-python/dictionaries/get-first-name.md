# Get First Name





See starter code docstring for requirements.

The person dictionary in this exercise will have the following structure:
```
{
    "last_name": str,
    "first_name": str
}
```

## Starter Code
```python
from typing import Dict


def get_first_name(person: Dict) -> str:
    """Returns the first name from a person dict
    
    Args:
        person: The person dict
                The dictionary has the keys 'first_name' and 'last_name'.
    Returns:
        The person's first name
    """
    return ""
```

## Tests
```python
from main import get_first_name


def test_get_first_name():
    jeff_smith = {
        "first_name": "Jeff",
        "last_name": "Smith"
    }
    assert get_first_name(jeff_smith) == "Jeff"

    john_mark = {
        "first_name": "John",
        "last_name": "Mark"
    }
    assert get_first_name(john_mark) == "John"
```
