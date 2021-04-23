# Keys with Target





The function's requirements are in the starter code docstring.

**Important**: The function's parameters need to be completed. Please look at the docstring to see what they should be called and what their data type is.

*Hint*:
Use the `in` operator and `dict.keys().` You can also use the `string.find()` method.

## Starter Code
```python
def get_keys_with():
    """Returns a list of keys in a dict which contain the target string.
    Args:
        target (str): The target substring to look for.
        thing (dict): A dictionary whose keys we want to search.
    Returns:
        (list) A list of all keys in the dictionary that contain the 
        target substring.
    """
    return None
```

## Tests
```python
from main import get_keys_with


def test_get_keys_with_has_proper_arguments():
    get_keys_with(target="blah", thing={"a": 1})


def test_get_keys_with():
    thing = {"a": 1, "b": 2, "aa": 3}
    result = get_keys_with("a", thing)
    assert result == ["a", "aa"]


def test_get_keys_with_nothing_found():
    thing = {"a": 1, "b": 2, "aa": 3}
    result = get_keys_with("c", thing)
    assert result == []


def test_get_keys_with_not_at_front_of_key_name():
    thing = {"aba": 0, "cbc": 1, "ddc": 2, "aab": 3}
    result = get_keys_with("b", thing)
    assert result == ["aba", "cbc", "aab"]


def test_get_keys_with_name():
    person = {
        "first_name": "Jeff",
        "last_name": "McNally",
        "age": 45,
        "eye_color": "blue",
        "name_of_pet": "Fluffy",
        "nickname": "Jeffy McNizzle"
    }
    result = get_keys_with("name", person)
    assert result == ["first_name", "last_name", "name_of_pet", "nickname"]
```
