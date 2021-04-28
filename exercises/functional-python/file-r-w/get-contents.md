# Get Contents





Files are saved on the hard drive so you can access them at a later date. All the data, even numbers, are stored as strings in files. We can have Python read from files. Let's assume for this problem that all the files have only one line of text in them.

The way we open files and read them is shown below:

```
with open("file_name.txt", "r") as f:
    contents = f.read()
```

`with` is a special keyword in Python, we don't need to worry about that just yet.

`open(file_name: str, mode: str)` is a function that allows us to open a file (specified by the `file_name`) in a particular mode. 

The modes important for now are:

- `"r"` -> read
- `"w"` -> write (overwrite)
- `"a"` -> append (write to bottom).

`as f` means we want to store the file object in a variable called `f`. You could call this variable anything.

`f.read()` will read the file and return it as a string, like the `input()` function.

The string data is then stored in a variable called `contents`. This can be called whatever.

# What to do

Assuming a file called `file.txt` already exists, open and read that file and return the contents.  The automated tests will create it for you, otherwise you have to create this file to test your solution.

**Fill in the blanks** using the example above as a reference.

## Starter Code
```python
def get_contents() -> str:
    with open("____.___", "_") as f:
        contents = f.____()
    
    return contents
```

## Tests
```python
import pytest
import os

from main import get_contents


FILENAME = 'file.txt'


@pytest.fixture(autouse=True)
def manage_file():
    yield
    if os.path.exists(FILENAME):
        os.remove(FILENAME)


def write_to_file(filename: str, contents: str) -> None:
    with open(filename, "w") as f:
        f.write(contents)


def test_get_contents_hello():
    write_to_file(FILENAME, "hello, world!")
    assert get_contents() == "hello, world!"


def test_get_contents_goodbye():
    write_to_file(FILENAME, "goodbye")
    assert get_contents() == "goodbye"


def test_get_contents_goodbye():
    write_to_file(FILENAME, "hello, goodbye")
    assert get_contents() == "hello, goodbye"
```
