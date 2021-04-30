# Generate Code Name



**Requirements:**
```eval_rst
- :ref:`fundamentals:load json data from a file`
- :ref:`fundamentals:accessing a value in a dictionary`
- :ref:`fundamentals:multiple elif`
- :ref:`fundamentals:format output text`
- :ref:`fundamentals:returning a value`

```


Read a JSON file containing information about an operative. Based on that information, generate a code name for them.

We store seemingly useless information about our operatives, but, we are able to generate code names for them based on that useless information. Depending on the values of particular attributes, we can assign them a code name.

Code names come in two parts.

1. An adjective and,
2. A noun

The code name is both words put together. i.e., `"Happy Foot"`

**The Adjective**

The first word is chosen based on the operatives favourite color. See the chart below.

```
Color    Adjective
------------------
White -> Happy
Blue  -> Sad
Red   -> Angry
Pink  -> Manly
```

**The Noun**

The next word is chosen based on their Imperial Academy scores.

```
Score                Noun
---------------------------
score < 50           Dropout
50 <= score < 60     Sloth
60 <= score < 70     Guppy
70 <= score < 80     Mountain
80 <= score < 90     Warlock
score >= 90          Beast
```

**Dictionary Specification**

```
operative = {
    "fav_color": str,
    "name": str,
    "academy_score": int,
    "eye_color": str
}
```

### Example case

An operative file containing:

```json
operative = {
    "fav_color": "White",
    "name": "Jeff Bridges",
    "academy_score": 43,
    "eye_color": "Blue"
}
```

 Would have the code name:

```
Happy Dropout
```

If testing manually, here is a [pre-made JSON file](https://github.com/mrgallo/python-exercises/assets/exercise-files/file-rw-generate-code-name.json) you can use. Change the relevant values to test the different outcomes.

## Starter Code
```python
import json


def generate_code_name(file_name: str) -> str:
    """Generates a code-name using information within the file of an operative.
    
    Args:
        file_name: The name of the operative's secret file.
        The file contains a JSON representation of the operative.
        See the "Dictionary Specification" section in the description.

    Returns:
        A generated code-name for the operative.
    """

    return ""
```

## Tests
```python
import pytest
import os
import random
import json


from main import generate_code_name


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


def test_generate_code_name_1():
    filename = "agent1-test.json"
    data = {
        "fav_color": "White",
        "name": "Jeff Bridges",
        "academy_score": 43,
        "eye_color": "Blue"
    }
    write_to_file(filename, json.dumps(data))

    assert generate_code_name(filename) == "Happy Dropout"


def test_generate_code_name_2():
    filename = "agent-test.json"
    data = {
        "fav_color": "Pink",
        "name": "Jeff Bridges",
        "academy_score": 67,
        "eye_color": "Blue"
    }
    write_to_file(filename, json.dumps(data))

    assert generate_code_name(filename) == "Manly Guppy"


def test_generate_code_name_2():
    filename = "agent-test.json"
    data = {
        "fav_color": "Pink",
        "name": "Jeff Bridges",
        "academy_score": 67,
        "eye_color": "Blue"
    }
    write_to_file(filename, json.dumps(data))

    assert generate_code_name(filename) == "Manly Guppy"


def test_generate_code_name_3():
    filename = "agent1-test.json"
    data = {
        "fav_color": "Blue",
        "name": "Jeff Bridges",
        "academy_score": 75,
        "eye_color": "Blue"
    }
    write_to_file(filename, json.dumps(data))

    assert generate_code_name(filename) == "Sad Mountain"


def test_generate_code_name_4():
    filename = "agent1-test.json"
    data = {
        "fav_color": "Red",
        "name": "Jeff Bridges",
        "academy_score": 99,
        "eye_color": "Blue"
    }
    write_to_file(filename, json.dumps(data))

    assert generate_code_name(filename) == "Angry Beast"


def test_generate_code_name_5():
    filename = "agent1-test.json"
    data = {
        "fav_color": "White",
        "name": "Jeff Bridges",
        "academy_score": 90,
        "eye_color": "Blue"
    }
    write_to_file(filename, json.dumps(data))

    assert generate_code_name(filename) == "Happy Beast"


def test_generate_code_name_6():
    filename = "agent1-test.json"
    data = {
        "fav_color": "White",
        "name": "Jeff Bridges",
        "academy_score": 60,
        "eye_color": "Blue"
    }
    write_to_file(filename, json.dumps(data))

    assert generate_code_name(filename) == "Happy Guppy"


def test_generate_code_name_7():
    filename = "agent1-test.json"
    data = {
        "fav_color": "White",
        "name": "Jeff Bridges",
        "academy_score": 50,
        "eye_color": "Blue"
    }
    write_to_file(filename, json.dumps(data))

    assert generate_code_name(filename) == "Happy Sloth"
```
