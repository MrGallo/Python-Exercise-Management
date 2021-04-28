# Update High Score





There is a file in the same directory of this code called `high_score.txt` and it stores the all-time high score for some game. The contents of the file are a simple integer.

Example of the contents of `high_score.txt`: 

```
57
```

Write the function that will take a `current_score` and compare it to the score in `high_score.txt`. If the current score is larger, that becomes the new high score. Over-write the previous high score by writing to the file.

**Remember**: File contents are stored as strings, even if they contain what appears to be integers.

## Starter Code
```python
def check_and_update_high_score(current_score: int) -> None:
    """Updates the high score file if the current score is larger.
    
    Args:
        current_score: The score of the game that just ended.
    """
    pass
```

## Tests
```python
import pytest
import os
import random

from main import check_and_update_high_score


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
    if os.path.exists("high_score.txt"):
        os.remove("high_score.txt")


def test_check_and_update_high_score_should_not_update_with_lower_score():
    filename = "high_score.txt"
    previous_high_score = "50"
    write_to_file(filename, previous_high_score)

    current_score = 40
    check_and_update_high_score(current_score)
    assert read_file(filename) == "50"


def test_check_and_update_high_score_should_update_with_higher_score():
    filename = "high_score.txt"
    previous_high_score = "50"
    write_to_file(filename, previous_high_score)

    current_score = 100
    check_and_update_high_score(current_score)
    assert read_file(filename) == "100"


def test_random_high_score():
    filename = "high_score.txt"
    previous_high_score = "50"
    write_to_file(filename, previous_high_score)

    current_score = random.randrange(51, 101)
    check_and_update_high_score(current_score)
    assert read_file(filename) == str(current_score)


def test_random_low_score():
    filename = "high_score.txt"
    previous_high_score = "50"
    write_to_file(filename, previous_high_score)

    current_score = random.randrange(0, 50)
    check_and_update_high_score(current_score)
    assert read_file(filename) == previous_high_score
```
