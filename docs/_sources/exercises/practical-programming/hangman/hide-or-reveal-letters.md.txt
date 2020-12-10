# Hide or reveal letters



**Requirements:**
```eval_rst
- :ref:`fundamentals:if, else`
- :ref:`fundamentals:string building and filtering`

```


The function specifications are in the starter-code docstring.

## Starter Code
```python
from typing import List


def reveal_letters(word: str, visible_letters: List[str]) -> str:
    """Reveal the given letters in a hidden word.
    
    Args:
        word: The word whose letters need to be revealed.
        visible_letters: A list of letters that should be visible in the word.
    
    Returns:
        The word with visible letters shown and all others blanked-out.
    
    Example:
        If the word is "hello" and visible_letters is the list ['e', 'o'],
        The resulting string would be "_ e _ _ o". Separate each character
        with a space to make it easier to read.
    """
    pass
```

## Tests
```python
from main import reveal_letters


def test_reveal_letters():
    assert reveal_letters("hello", ['e', 'o']) == "_ e _ _ o"
    assert reveal_letters("hello", []) == "_ _ _ _ _"
    assert reveal_letters("abc", ['a', 'b', 'c']) == "a b c"
```
