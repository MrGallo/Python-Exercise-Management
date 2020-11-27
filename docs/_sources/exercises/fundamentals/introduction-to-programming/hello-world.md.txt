# Hello, World!

**Topic:** 
```eval_rst
:ref:`fundamentals:output a message`

```



One of the most important parts of a computer program is the ability for the computer to talk to the user (the person running the program). In Python, this is achieved using the `print()` function. The `print()` function will will output anything you want to the terminal screen (it does not activate your printer). 


### Your task
1. Run the starter code to see an example of what it looks like to print something to the terminal. The code, as it is, should output the following:
    ```
    Hello,
    ```
2. In addition to the output that is already there, make the program print out `"World!"`. The result should look like:
    ```
    Hello,
    World!
    ```

## Starter Code
```python
print("Hello,")
print()
```

## Tests
```python
from exercise.fixtures import captured_output


def test_hello_world(captured_output):
    assert captured_output() == "Hello,\nWorld!"
```
