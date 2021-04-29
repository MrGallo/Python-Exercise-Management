# f(x) = x + 4



**Requirements:**
```eval_rst
- :ref:`fundamentals:mathematical operations`

```


A function is defined using the keyword `def`. A function is a sub program that can be called into action whenever we (the programmer) want. 

In its simplest form, a function:

1. takes input
2. processes data, and 
3. returns a result.

This is similar to math. Given the mathematical function `f(x) = x + 4`, when we call the function with `f(6)` we get a result of 10. In programming we can define similar functions but use a variety of data for `x` and return more than just numbers.

## Your task

The function given is set up to receive an integer value for x. All you have to do is modify the return statement to **have the function return `x + 4` .** The doc-string enclosed in the triple-quotes `"""` is optional and is there so that other programmers can quickly understand what the function needs to do its job and what it returns as a result.

## Testing your code
After the function, and **un-indented,** call your function like above and print it out.

```python
print(f(5))
```

Now hit run. The program will print the result of your function.

## Starter Code
```python
def f(x: int) -> int:
    """Returns the value of x plus 4
    
    Args:
        x: An integer
    Returns:
        Another integer, x + 4
    """
    return x
```

## Tests
```python
from main import f


def test_f():
    assert f(5) == 9
    assert f(6) == 10
    assert f(-4) == 0
```
