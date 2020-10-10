# name
Hello, World!

# topic
output a message

# requirements


# description
One of the most important parts of a computer program is the ability for the computer to talk to the user (the person runnin the program). In Python, this is achieved using the `print()` function. The `print()` function will will output anything you want to the terminal screen (it does not activate your printer). 

Run the starter code to see an example of what it looks like to print something to the terminal.

### Your task
In addition to the print statement that is already there, make the program print out `"world!"`. The result should look like:

```
Hello,
World!
```

# starter code
```python
print("Hello,")
print()
```

# tests
```python
from exercise.fixtures import captured_output


def test_hello(captured_output):
    assert captured_output() == "Hello,\nWorld!"

```
