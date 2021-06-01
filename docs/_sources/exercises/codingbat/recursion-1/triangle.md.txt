# triangle





We have triangle made of blocks. The topmost row has 1 block, the next row down has 2 blocks, the next row has 3 blocks, and so on. Compute recursively (no loops or multiplication) the total number of blocks in such a triangle with the given number of rows.

```
triangle(0) -> 0
triangle(1) -> 1
triangle(2) -> 3
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p194781) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def triangle(rows: int) -> int:
    pass


result = triangle(0)
print(result)
```

## Tests
```python
from main import triangle


def test_triangle_1():
    assert triangle(0) == 0


def test_triangle_2():
    assert triangle(1) == 1


def test_triangle_3():
    assert triangle(2) == 3


def test_triangle_4():
    assert triangle(3) == 6


def test_triangle_5():
    assert triangle(4) == 10


def test_triangle_6():
    assert triangle(5) == 15


def test_triangle_7():
    assert triangle(6) == 21


def test_triangle_8():
    assert triangle(7) == 28
```
