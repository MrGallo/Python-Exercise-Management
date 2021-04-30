# Load Code Name



**Requirements:**
```eval_rst
- :ref:`fundamentals:load json data from a file`
- :ref:`fundamentals:accessing a value in a dictionary`
- :ref:`fundamentals:returning a value`

```


There is a JSON file that stores information about a secret operative. Your task is to load the JSON file using the python `json` library and find this secret operative's `code_name`. Your function will extract and return their code name.

If doing this exercise manually, here is a [pre-made JSON](https://github.com/mrgallo/python-exercises/assets/exercise-files/file-rw-code-name.json) file to practice with.

## Starter Code
```python
import json


def extract_code_name(file_name: str) -> str:
    """Extracts the operative's code name from a JSON file.
    
    Args:
        file_name: The name of the file with the operative's information.
    Returns:
        The operative's code name. The dictionary loaded from the JSON
        file will have a key of "code_name".
    """
    return ""
```

## Tests
```python
import pytest
import os
import random
import json


from main import extract_code_name


def remove_file(file_name: str) -> None:
    if os.path.exists(file_name):
        os.remove(file_name)


def read_file(filename: str) -> None:
    with open(filename, "r") as f:
        return f.read().strip()


def write_to_file(filename: str, contents: str) -> None:
    with open(filename, "w") as f:
        f.write(contents)


@pytest.fixture(autouse=True)
def clear_test_files():
    yield
    files = os.listdir()
    for f in files:
        if f.endswith("-test.json"):
            os.remove(f)


def test_extract_code_name_1():
    filename = "agent1-test.json"
    data = {
        "age": 45,
        "specialty": "stealth",
        "code_name": "Sneaky McGee",
        "preferred_snack": "pizza"
    }
    write_to_file(filename, json.dumps(data))

    assert extract_code_name(filename) == "Sneaky McGee"


def test_extract_code_name_2():
    filename = "agent2-test.json"
    data = {
        "age": 67,
        "specialty": "survival",
        "code_name": "Unkillable Monster",
        "preferred_snack": "raw flesh"
    }
    write_to_file(filename, json.dumps(data))

    assert extract_code_name(filename) == "Unkillable Monster"


def test_extract_code_name_3():
    filename = f"agent{random.randrange(0, 100)}-test.json"
    data = {
        "age": 24,
        "specialty": "being nice",
        "code_name": "Fluffy Bunny",
        "preferred_snack": "cotton candy"
    }
    write_to_file(filename, json.dumps(data))

    assert extract_code_name(filename) == "Fluffy Bunny"
```
