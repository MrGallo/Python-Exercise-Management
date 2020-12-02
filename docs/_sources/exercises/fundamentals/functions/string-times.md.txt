# String Times

**Topic:** 
```eval_rst
:ref:`fundamentals:defining parameters`

```



If you ran the function defined in the starter code, you would get a `NameError` for both the `n` and `string` variables used in the function. The body of the function is good as it is. What is missing from this function definition is its parameters. The question is "what does this function require to do its job?" Then the next question is "how should we name those parameters?"

## Starter Code
```python
def string_times() -> str:
    """Return a string repeated n times."""
    new_string = ""
    for i in range(n):
        new_string += string
    return new_string
```

## Tests
```python
from main import string_times


def test_string_times():
    assert string_times("hello", 2) == "hellohello"
    assert string_times("x", 5) == "xxxxx"
```
