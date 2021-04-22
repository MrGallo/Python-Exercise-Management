# Reverse Last Name



**Requirements:**
```eval_rst
- :ref:`fundamentals:defining a function`
- :ref:`fundamentals:defining parameters`

```


### Important!

For this problem, you need to add the appropriate parameters to the `reverse_last_name` function definition **as well as** complete the code for the function body.

### Dictionary Structure

The dictionary passed to the function will have the following structure:

```
{
    "first_name": str,
    "last_name": str
}
```

## Starter Code
```python
def reverse_last_name():
    """Gets the person's last name reversed

    Args:
        person: Person dict with first and last name.
                The dictionary has the keys 'first_name' and 'last_name'.
    Returns:
        Last name reversed and capitalized (first letter only).
        For example, "Smith" becomes "Htims".
    """
    return ""
```

## Tests
```python
from main import reverse_last_name


def test_reverse_last_name():
    jeff_smith = {
        "first_name": "Jeff",
        "last_name": "Smith"
    }
    assert reverse_last_name(jeff_smith) == "Htims"

    john_mark = {
        "first_name": "John",
        "last_name": "Mark"
    }
    assert reverse_last_name(john_mark) == "Kram"
```
