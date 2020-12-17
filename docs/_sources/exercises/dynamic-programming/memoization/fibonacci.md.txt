# Fibonacci





The Fibonacci sequence is `1, 1, 2, 3, 5, 8, ...`. Each successive number is found by adding the previous two. Create a recursive algorithm to compute the `n`th number in the Fibonacci sequence. Use memoization to get the last test to pass in a respectable about of time.

```
fib(1) -> 1
fib(2) -> 1
fib(3) -> 2
fib(4) -> 3
fib(5) -> 5
```

You can learn more from Free Code Camp's [Dynamic Programming](https://www.youtube.com/watch?v=oBt53YbR9Kk) video.

## Starter Code
```python
def fib(n: int) -> int:
    pass
```

## Tests
```python
from main import fib


def test_fib():
    assert fib(6) == 8
    assert fib(7) == 13
    assert fib(8) == 21
    assert fib(50) == 12586269025
    assert fib(100) == 354224848179261915075
```
