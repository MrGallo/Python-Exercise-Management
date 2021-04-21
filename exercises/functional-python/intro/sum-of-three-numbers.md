# Sum of three numbers





Write a function that takes three numbers as arguments and returns their sum.

**Example function call**

```
add(2, 3, 6)
```

**Example result**

```
11
```

**Credit**
Adapted from www.snakify.org

## Starter Code
```python
# This function takes two numbers and returns their sum:
def add(a: int, b: int) -> int:
    """Returns the sum of two integers.
    
    Args:
        a: a number
        b: a number
    Returns:
        Sum of the numbers
    """
    return a + b
    

# Can you change it so it can take and return the sum of three numbers?
```

## Tests
```python
from main import add


def test_add():
    assert add(1, 1, 1) == 3
    assert add(1, 2, 3) == 6
    assert add(-1, 0, 1) == 0
```
