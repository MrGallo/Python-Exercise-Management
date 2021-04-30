# Read Multiple Lines



**Requirements:**
```eval_rst
- :ref:`fundamentals:read multiple lines from a file`
- :ref:`fundamentals:convert strings to numbers`
- :ref:`fundamentals:loop with an accumulator variable`
- :ref:`fundamentals:returning a value`

```


The files that will be read as part of this exercise contain multiple lines, one integer per line.

For example, this could be the contents of a file:

```
56
12
8
234
8
3
```

Your program needs to read those integers in and return the sum of the numbers.

In this case, the answer would be:

```
321
```

### How to do it

This is accomplished the same way as reading in one line, except you need to **use a for loop** to iterate through each line of the file.

Here is a working piece of code, assuming a file called `file.txt` exists and has integers on each line.

**file.txt**

```
1
2
3
4
```
**example_code.py**

```
with open("file.txt", "r") as f:
    for line in f:
        print(line)
```

**output**

```
1
2
3
4
```

Instead of printing the numbers, add them to a total.

## Starter Code
```python
def add_nums_from_file(file_name: str) -> int:
    """Returns the sum of all integers in the given file.
    
    Args:
        file_name: The name of the file.
    Returns:
        Sum of all the numbers in the file.
    """
    return 0
```

## Tests
```python
import pytest
import os
import random


from main import add_nums_from_file


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
        if f.endswith(".test_txt"):
            os.remove(f)


def test_add_nums_from_file_1():
    filename = "numbers.test_txt"
    numbers = [1, 2, 3]
    content = "\n".join(map(str, numbers))
    write_to_file(filename, content)

    assert add_nums_from_file(filename) == 6


def test_add_nums_from_file_2():
    filename = "numbers_2.test_txt"
    numbers = [0, 0, 0, 0, 0]
    content = "\n".join(map(str, numbers))
    write_to_file(filename, content)

    assert add_nums_from_file(filename) == 0


def test_add_nums_from_file_3():
    filename = "numbers_2.test_txt"
    numbers = [2, 4, 6, 8, 10]
    content = "\n".join(map(str, numbers))
    write_to_file(filename, content)

    assert add_nums_from_file(filename) == 30


def test_add_nums_from_file_random():
    filename = "numbers_2.test_txt"
    numbers = [random.randrange(0, 101) for _ in range(10)]
    content = "\n".join(map(str, numbers))
    write_to_file(filename, content)

    assert add_nums_from_file(filename) == sum(numbers)
```
