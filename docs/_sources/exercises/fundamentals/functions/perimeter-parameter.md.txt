# Perimeter Parameter

**Topic:** 
```eval_rst
:ref:`fundamentals:defining parameters`

```

**Requirements:**
```eval_rst
- :ref:`fundamentals:passing arguments`

```


The starter code is missing a parameter in the definition of the `side_length_from_perimeter` function. Notice if you run the code, it will give you a `TypeError`. 

Please put, in its proper place, the perimeter parameter.

## Starter Code
```python
def side_length_from_perimeter() -> float:
    """Get the side length of a square by its perimeter.
    
    Args:
        perimeter (float): The perimiter of the square.
    
    Returns:
        The side length of the square.
    """
    return perimeter / 4


length = side_length_from_perimeter(12)
print(length)  # should be 3
```

## Tests
```python
from main import side_length_from_perimeter


def test_side_length_from_perimeter():
    assert side_length_from_perimeter(16) == 4
    assert side_length_from_perimeter(12) == 3
    assert side_length_from_perimeter(36) == 9
```
