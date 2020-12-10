# Word reveal



**Requirements:**
```eval_rst
- :ref:`fundamentals:defining a function`
- :ref:`fundamentals:defining parameters`

```


When the player wins or loses, the game will output a message telling them what the secret word was. The function body is complete, it returns a message indicating the secret word. Your job is to complete the function definition. The function is supposed to be named `word_reveal_message` and it has a parameter-variable called `word`. Fill in those blanks after the word `def`.

## Starter Code
```python
def ________________(______):
    """Creates a message revealing the secret word.
    
    Args:
        word: the word being revealed.
    
    Returns:
        A message revealing the secret word.
    
    Example: 
        "The secret word was 'orange'."
    """
    return f"The secret word was'{word}'."
```

## Tests
```python
from main import word_reveal_message


def test_word_reveal_message():
    assert "'orange'" in word_reveal_message("orange")
    assert "'blah'" in word_reveal_message("blah")
    assert "''" in word_reveal_message("")
```
