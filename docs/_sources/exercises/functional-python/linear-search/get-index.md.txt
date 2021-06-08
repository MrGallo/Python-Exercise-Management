# Get Index







## Starter Code
```python
from typing import List


def get_index(numbers: List[int], target: int) -> int:
    """Get the index of the first occurance of the specified target value.
    
    Args:
        numbers: the list to search.
        target: the value to search for.
    
    Returns:
        The index of the found element. -1 if not found.

    Note: do not use the .index or .find methods.
    """
    pass
```

## Tests
```python
import random

from main import get_index

# only for https://replit.com/@DanielGallo/Python-Exercise-Runner
from exercise.fixtures import source_code_matches


def test_returns_negative_1_for_empty_list():
    assert get_index([], 99) == -1


def test_returns_negative_1_if_not_found():
    assert get_index([1, 2, 3, 4], 99) == -1


def test_correct_index_at_front():
    assert get_index([99, 2, 3, 4], 99) == 0


def test_correct_index_at_back():
    assert get_index([1, 2, 3, 99], 99) == 3


def test_correct_index_in_middle():
    assert get_index([1, 2, 99, 4, 5], 99) == 2


def test_first_occurance_index_only():
    assert get_index([99, 2, 99, 4, 5], 99) == 0


def test_acceptance():
    for _ in range(100):
        length = random.randrange(1, 100)
        numbers = [random.randrange(1000) for _ in range(length)]
        target_index = random.randrange(length)
        target = -1
        numbers.insert(target_index, -1)
        assert get_index(numbers, -1) == target_index


# only for https://replit.com/@DanielGallo/Python-Exercise-Runner
def test_code_not_contains_index_or_find_method():
    assert len(source_code_matches(r'\.\s?index\s?\(')) == 0
    assert len(source_code_matches(r'\.\s?find\s?\(')) == 0
```
