# The Number N

**Topic:** 
```eval_rst
:ref:`fundamentals:returning a value`

```

**Requirements:**
```eval_rst
- :ref:`fundamentals:handling return values`

```


The starter code makes several calls to two functions that are not returning the proper values. `the_sum` should be `5` and `the_product` should be `6`. Modify the functions to return `2` and `3` respectively.

## Starter Code
```python
def the_number_two():
    return 0


def the_number_three():
    return 0


the_sum = the_number_two() + the_number_three()
the_product = the_number_two() * the_number_three()

print(the_sum)  # should be 5
print(the_product)  # should be 6
```

## Tests
```python
from main import the_number_two, the_number_three


def test_the_number_two():
    assert the_number_two() == 2


def test_the_number_three():
    assert the_number_three() == 3
```
