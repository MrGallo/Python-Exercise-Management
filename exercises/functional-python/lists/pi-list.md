# Pi List



**Requirements:**
```eval_rst
- :ref:`fundamentals:creating a list`
- :ref:`fundamentals:returning a value`

```


Complete the function so it returns a list of the first three digits of Pi. *Hint: don't create a list of the number `314`, make a list of each digit separated.*

## Starter Code
```python
from typing import List


def get_pi() -> List[int]:
    """Returns the first three digits of Pi in a list"""
    return None
```

## Tests
```python
from main import get_pi


def test_get_pi():
    assert get_pi() == [3, 1, 4]
```
