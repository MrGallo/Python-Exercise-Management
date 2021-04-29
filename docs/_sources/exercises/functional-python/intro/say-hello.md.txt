# say_hello



**Requirements:**
```eval_rst
- :ref:`fundamentals:format output text`

```


Often, we need to include values into strings to make things easier to read whenever someone uses our program. For example, showing the value of the area of a rectangle by itself is not helpful.

```
45.5
```

However, if we included the value into a string, it would be easier to read.

```
The area of the rectangle is 45.5 meters squared.
```

There are a number of ways to include the values of variables in strings. The different approaches have pros and cons in different situations, but, their final result is identical. You can choose to learn and use them all, or stick to one.

```python
name = "Frank"
age = 56

f_strings_approach = f"This is {name}. He is {age} years old."  # python 3.6+
dot_format_approach = "This is {}. He is {} years old.".format(name, age)
concatenate_approach = "This is " + name + ". He is " + str(age) + " years old."
```

```python
# All three approaches produce the identical string
"This is Frank. He is 56 years old."
```

## Your task

The function in the code window is set up to receive a `name` (string) and return a result that is a string. Create and return the message `"Hello, {name}!"` by inserting the variable `name` into the string using one of the approaches above.

## Starter Code
```python
def say_hello(name: str) -> str:
    """Creates a greeting for a friend.
    
    Args:
        name: The name of someone to say hi to
    Returns:
        A greeting in the format "Hello, {name}!"
    """
    return
```

## Tests
```python
from main import say_hello


def test_say_hello():
    assert say_hello("Dave") == "Hello, Dave!"
    assert say_hello("") == "Hello, !"
    assert say_hello("Samuel") == "Hello, Samuel!"
```
