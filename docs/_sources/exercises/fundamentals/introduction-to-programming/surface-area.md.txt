# Surface Area

**Topic:** 
```eval_rst
:ref:`fundamentals:mathematical operations`

```



Multiplication in Python is done with the asterisk character (`*`). For example, in Python, the expression `5 * 3` will evaluate to `15`.

The starter code shown below is quite wrong. It's supposed to calulate the surface area of a `10 cm` by `25 cm` rectangle. Go and fix the equation on line 1.

## Starter Code
```python
surface_area = 10 + 25
print(f"The surface area is {surface_area} cm^2")
```

## Tests
```python
from exercise.fixtures import captured_output


def test_answer_should_be_250(captured_output):
    assert captured_output() == "The surface area is 250 cm^2"
```
