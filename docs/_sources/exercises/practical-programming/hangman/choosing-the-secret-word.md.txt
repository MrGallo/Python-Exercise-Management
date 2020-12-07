# Choosing the secret word



**Requirements:**
```eval_rst
- :ref:`fundamentals:accessing list elements`
- :ref:`fundamentals:returning a value`

```


In the `main` function we have:

```python
secret_word = get_random_word(WORD_LIST)
```

When we start the program, we need the computer to select a random word and save it as `secret_word`. Take note that this function requires a list of words be given to it so it can pick one at random. The function is supposed to return one of those words. Complete the function in the starter code. *Hint: use `random.choice` or `random.randint`.*

## Starter Code
```python
from typing import List


def get_random_word(word_list: List[str]) -> str:
    """Gets a random word.
    
    Args: 
        word_list: the list from which to get the word.
    
    Returns:
        A single word.
    """
    pass
```

## Tests
```python
from main import get_random_word


def test_get_random_word():
    choices = list("abcdefg")
    chosen = set()
    for _ in range(100):
        chosen.add(get_random_word(choices))
    assert chosen == set(choices)
```
