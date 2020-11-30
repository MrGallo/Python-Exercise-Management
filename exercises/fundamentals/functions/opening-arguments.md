# Opening arguments

**Topic:** 
```eval_rst
:ref:`fundamentals:passing arguments`

```

**Requirements:**
```eval_rst
- :ref:`fundamentals:calling a function`

```


The starter code defines a function that requires an argument to be passed to it when you call it. In programming, this information is literally called an **argument**, rergardless of what you are passing to the function.

If you run the code as-is, the error will tell you are missing one required positional argument. Be a good defense lawyer and pass the function an argument, the string `"my client is innocent"`.

The function should run and output the following:

```
The defense will commence with their opening arguments:
Your Honour, my client is innocent.
```

You should experiment by passing the function different arguments and taking note how the output changes.

## Starter Code
```python
def give_argument(argument: str) -> None:
    print("The defense will commence with their opening arguments:")
    print(f"Your Honour, {argument}.")


give_argument()
```

## Tests
```python
from exercise.fixtures import captured_output


def test_give_argument(captured_output):
    assert captured_output().endswith("Your Honour, my client is innocent.")
```
