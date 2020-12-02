# Skyline

**Topic:** 
```eval_rst
:ref:`fundamentals:defining a function`

```

**Requirements:**
```eval_rst
- :ref:`fundamentals:calling a function`

```


The starter code has a sideways skyline of a city with ASCII art buildings. There are only three unique building types and some are repeated. This means we have a situation where each building can be converted into its own function. Create functions called `building_a`, `building_b` and `building_c`. Then call those functions in the order they originally appeared in the skyline (`ACBACC`).

## Starter Code
```python
# building A
print("-----------")
print("**********|")
print("**********|")
print("-----------")

# building C
print("--------")
print("' '' ''|")
print("--------")

# building B
print("###############")
print("###############")

# building A
print("-----------")
print("**********|")
print("**********|")
print("-----------")

# building C
print("--------")
print("' '' ''|")
print("--------")

# building C
print("--------")
print("' '' ''|")
print("--------")
```

## Tests
```python
from exercise.fixtures import captured_output, source_code_matches


def test_output(captured_output):
    assert captured_output() == """-----------
**********|
**********|
-----------
--------
' '' ''|
--------
###############
###############
-----------
**********|
**********|
-----------
--------
' '' ''|
--------
--------
' '' ''|
--------"""

def test_code_contains_functions():
    assert source_code_matches("def building_a")
    assert source_code_matches("def building_b")
    assert source_code_matches("def building_c")
```
