# Create Person



**Requirements:**
```eval_rst
- :ref:`fundamentals:creating a dictionary`
- :ref:`fundamentals:returning a value`

```




## Starter Code
```python
from typing import Dict


def create_person_dict(first_name: str, last_name:str) -> Dict:
    """Creates a person dictionary with the given first and last name.
    
    Args:
        first_name: The person's first name
        last_name: The person's last name
    Returns:
        Person represented as a dictionary
        with keys "first_name" and "last_name".
    """
    return {}
```

## Tests
```python
from main import create_person_dict


def test_has_proper_keys():
    result = create_person_dict("Jeff", "Smith")

    for key in result.keys():
        assert key in ("first_name", "last_name")


def test_assigns_proper_values_to_keys_jeff_smith():
    result = create_person_dict("Jeff", "Smith")

    expected = {
        "first_name": "Jeff",
        "last_name": "Smith"
    }
    
    assert result == expected


def test_assigns_proper_values_to_keys_john_mark():
    result = create_person_dict("John", "Mark")

    expected = {
        "first_name": "John",
        "last_name": "Mark"
    }

    assert result == expected
```
