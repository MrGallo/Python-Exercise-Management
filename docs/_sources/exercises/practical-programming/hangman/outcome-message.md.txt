# Outcome message



**Requirements:**
```eval_rst
- :ref:`fundamentals:if, else`
- :ref:`fundamentals:defining a function`
- :ref:`fundamentals:defining parameters`
- :ref:`fundamentals:returning a value`

```


When the game is over, the player will recieve a message based on their outcome. The function will display the result message which is dependant on whether or not the player won or lost. The function is supposed to be called `outcome_message` and have a parameter-variable called `result`. Result will be a string containing `"win"` or `"lose"`. Fill in the function definition and complete the function. Return `"Congratulations! You won!"` if they won, otherwise return `"Sorry. You lost."`.

## Starter Code
```python
def _____________(______):
    """Creates a message based on the player's outcome.
    
    Args:
        result: Either 'win' or 'lose'.
    
    Returns:
        An appropriate message based on the player's outcome.
    """
    pass
```

## Tests
```python
from main import outcome_message


def test_outcome_message():
    assert outcome_message("win") == "Congratulations! You won!"
    assert outcome_message("lose") == "Sorry. You lost."
```
