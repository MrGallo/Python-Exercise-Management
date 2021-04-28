# Friendly File





Imagine that there are a number of files on the hard disk. Some files are **friendly** and some files are **MEAN** and some are neutral. All the files will contain only one word. Depending on which word, we can determine if they are `friendly`, `mean`, or `neutral`.

A **friendly file** has one the following words:

```
hello
howdy
hi
```

A **mean** file has one of the following words:

```
boo
leave
blah
```

A **neutral** file will contain any other word.

See the starter code docstring for more information.

## Starter Code
```python
def friendly_mean_or_neutral(file_name: str) -> str:
    """Determines if a file is friendly, mean, or neutral.
    
    Args:
        file_name: The name of the file to check.
    Returns:
        "friendly", "mean" or "neutral" depending on the contents.
    """
    return None
```

## Tests
```python
import pytest
import os
import uuid


from main import friendly_mean_or_neutral


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


def test_friendly_mean_or_neutral_friendly():
    friendly_msgs = ["hello", "howdy", "hi"]

    for msg in friendly_msgs:
        filename = f"{uuid.uuid4().hex}.test_txt"
        write_to_file(filename, msg)
        assert friendly_mean_or_neutral(filename) == "friendly"


def test_friendly_mean_or_neutral_mean():
    mean_msgs = ["boo", "leave", "blah"]

    for msg in mean_msgs:
        filename = f"{uuid.uuid4().hex}.test_txt"
        write_to_file(filename, msg)
        assert friendly_mean_or_neutral(filename) == "mean"



def test_friendly_mean_or_neutral_neutral():
    neutral_msgs = ["apples", "oranges", "bananas"]

    for msg in neutral_msgs:
        filename = f"{uuid.uuid4().hex}.test_txt"
        write_to_file(filename, msg)
        assert friendly_mean_or_neutral(filename) == "neutral"
```
