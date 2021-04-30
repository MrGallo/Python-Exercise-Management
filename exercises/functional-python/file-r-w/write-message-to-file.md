# Write Message to File



**Requirements:**
```eval_rst
- :ref:`fundamentals:write to a file`

```


Use the same pattern learned in the previous exercise to write to the file.

`open(file_name: str, mode: str)`

## Starter Code
```python
def write_msg_to_file(msg: str, file_name: str) ->< None>:
    """Will write a message to a file
    
    Args:
        msg: The message to write.
        file_name: The name of the file to write the message in.
    """
    pass
```

## Tests
```python
import pytest
import os
import uuid


from main import write_msg_to_file


def remove_file(file_name: str) -> None:
    if os.path.exists(file_name):
        os.remove(file_name)


def read_file(filename: str) -> None:
    with open(filename, "r") as f:
        return f.read().strip()


@pytest.fixture(autouse=True)
def clear_test_files():
    yield
    files = os.listdir()
    for f in files:
        if f.endswith(".test_txt"):
            os.remove(f)


def test_write_msg_to_file_hello():
    filename = "hello.test_txt"
    contents = "hello world!"
    write_msg_to_file(contents, filename)
    assert read_file(filename) == contents


def test_write_msg_to_file_acceptance():
    for _ in range(10):
        filename = f"{uuid.uuid4().hex}.test_txt"
        contents = f"{uuid.uuid4().hex}"
        write_msg_to_file(contents, filename)
        assert read_file(filename) == contents
```
