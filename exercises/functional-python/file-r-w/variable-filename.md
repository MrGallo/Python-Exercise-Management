# Variable Filename





This will be the same as the last exercise, except you will be given the name of the file int the parameter variable `file_name`. Return the contents of the given file.

## Starter Code
```python
def get_contents(file_name: str) -> str:
    """Returns the contents of the given file.
    
    Args:
        file_name: The name of the file to fetch the contents.
    Returns:
        The contents of the given file as a string.
    """
    return ""
```

## Tests
```python
import pytest
import os
import uuid


from main import get_contents


def remove_file(file_name: str) -> None:
    if os.path.exists(file_name):
        os.remove(file_name)


def write_to_file(filename: str, contents: str) -> None:
    with open(filename, "w") as f:
        f.write(contents)


@pytest.fixture(autouse=True)
def clear_test_files():
    yield
    files = os.listdir()
    for f in files:
        if f.endswith(".test_txt"):
            os.remove(f)


def test_get_contents_hello():
    filename = "blah.test_txt"
    write_to_file(filename, "hello, world!")
    assert get_contents(filename) == "hello, world!"


def test_get_contents_goodbye():
    filename = "342fsafs6.test_txt"
    write_to_file(filename, "goodbye")
    assert get_contents(filename) == "goodbye"


def test_get_contents_goodbye():
    filename = "hello-goodbye.test_txt"
    write_to_file(filename, "hello, goodbye")
    assert get_contents(filename) == "hello, goodbye"


def test_get_contents_random_filename():
    filename = f"{uuid.uuid4().hex}.test_txt"
    write_to_file(filename, "cant use if statements for this!")
    assert get_contents(filename) == "cant use if statements for this!"
```
