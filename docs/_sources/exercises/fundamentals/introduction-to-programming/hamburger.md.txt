# Hamburger

**Topic:** 
```eval_rst
:ref:`fundamentals:output a message`

```



With the starter code (given in `main.py`) your program outputs an empty hamburger. You goal is to create a complete hamburger.

1. Run the program and observe the output. It should be as follows:
    ```
    (--Bun--)

    (--Bun--)
    ```
    Notice the empty space. This empty line comes from the empty `print()` function.
2. Place the string `"Hamburger"` inside that empty `print()` function.

## Starter Code
```python
print("(--Bun--)")
print()
print("(--Bun--)")
```

## Tests
```python
from exercise.fixtures import captured_output


def test_hamburger(captured_output):
    assert captured_output() == "(--Bun--)\nHamburger\n(--Bun--)"
```
