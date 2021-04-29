# Empty Dict



**Requirements:**
```eval_rst
- :ref:`fundamentals:creating a dictionary`
- :ref:`fundamentals:returning a value`

```


Requirements in starter code docstring.

## Starter Code
```python
from typing import Dict


def create_an_empty_dictionary() -> Dict:
    """Creates an empty dictionary
    
    Args: 
        None
    Returns:
        Empty dictionary
    """
    return None
```

## Tests
```python
from main import create_an_empty_dictionary


def test_create_an_empty_dictionary():
    assert create_an_empty_dictionary() == {}
```
