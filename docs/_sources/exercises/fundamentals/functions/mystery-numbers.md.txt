# Mystery Numbers

**Topic:** 
```eval_rst
:ref:`fundamentals:returning a value`

```

**Requirements:**
```eval_rst
- :ref:`fundamentals:handling return values`

```


The starter code has two incomplete functions. They have the keyword `pass` as a place-holder. Remove `pass` and return the numbers they should return to solve the math riddle in the starter code. The tests are as follows:

```
assert mystery_number_a() + mystery_number_a() == 16
assert mystery_number_a() * mystery_number_b() == 16
```

## Starter Code
```python
def mystery_number_a():
    pass


def mystery_number_b():
    pass


sixteen = mystery_number_a() + mystery_number_a()  # should be 16
sixteen_again = mystery_number_a() * mystery_number_b()  # should be 16

print(sixteen)
print(sixteen_again)
```

## Tests
```python
from main import mystery_number_a, mystery_number_b


def test_mystery_number_a():
    assert mystery_number_a() + mystery_number_a() == 16


def test_mystery_number_b():
    assert mystery_number_a() * mystery_number_b() == 16
```
