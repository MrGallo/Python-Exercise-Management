# Hello, Goodbye

**Topic:** 
```eval_rst
:ref:`fundamentals:output a message`

```



The print function in the starter code provided (`main.py`) currently prints out the string `"Hello"`. Modify the code, so instead of printing out `"Hello"`, it prints out `"Goodbye"`. 

1. Run the code and observe the fact the output says `"Hello"`.
2. Change the string in the `print()` function to `"Goodbye"`.
3. Run the program again to observe the change. The output should no longer include `Hello`, only `Goodbye`. Expected output:
    ```
    Goodbye
    ```

## Starter Code
```python
print("Hello")
```

## Tests
```python
from exercise.fixtures import captured_output


def test_hello_goodbye(captured_output):
    assert captured_output() == "Goodbye"
```
