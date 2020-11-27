# Hello, goodbye

**Topic:** 
```eval_rst
:ref:`fundamentals:calling a function`

```



The Beatles (from the 60's) have a song called "Hello, Goodbye". Part of the lyrics are:

```
Hello,
goodbye.
Hello,
goodbye.
Hello,
goodbye.
Hello,
goodbye.
```

Inspiring, I know. 

The starter code has a function defined that will print one set of "Hello, goodbye.". The starter code calls the function only once. Unfortunately, to make a hit song, you need to repeat things many times. In this case it needs to be called a total of four times.

All you need to do is call the function `hello_goodbye` four times to achieve the lyrics as shown above.

## Starter Code
```python
def hello_goodbye():
    print("Hello,")
    print("goodbye.")


hello_goodbye()
```

## Tests
```python
from exercise.fixtures import captured_output


def test_hello_goodbye(captured_output):
    assert captured_output() == ("Hello,\ngoodbye.\n" * 4).strip()
```
