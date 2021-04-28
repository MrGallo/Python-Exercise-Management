# Write to File





When you write to a file, you need to open the file in the "write" mode using the string `"w"`.

Write mode will overwrite everything in the file if it exists. If the file does not exist, it will be created.

Use the following pattern to write to a file.

```
with open("filename.txt", "w") as f:
    f.write("Hello")
```

What to do

The file you write to will be called `"file.txt"` and you are to write the message `"Hello, file!"`

## Starter Code
```python
def write_to_file():
    """Writes "Hello, file!" to a file called "file.txt."""
    
    with open("____.___", "_") as f:
        f.____("____________")
```

## Tests
```python
import pytest
import os


from main import write_to_file


def remove_file(file_name: str) -> None:
    if os.path.exists(file_name):
        os.remove(file_name)


def test_write_to_file_contains_hello_file():
    write_to_file()

    with open('file.txt') as f:
        assert f.read().strip() == "Hello, file!"
    
    remove_file("file.txt")
```
