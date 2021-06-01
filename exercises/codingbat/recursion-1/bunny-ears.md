# bunny_ears





We have a number of bunnies and each bunny has two big floppy ears. We want to compute the total number of ears across all the bunnies recursively (without loops or multiplication).

```
bunny_ears(0) -> 0
bunny_ears(1) -> 2
bunny_ears(2) -> 4
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p183649) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def bunny_ears(bunnies: int) -> int:
    pass


result = bunny_ears(0)
print(result)
```

## Tests
```python
from main import bunny_ears


def test_bunny_ears_1():
    assert bunny_ears(0) == 0


def test_bunny_ears_2():
    assert bunny_ears(1) == 2


def test_bunny_ears_3():
    assert bunny_ears(2) == 4


def test_bunny_ears_4():
    assert bunny_ears(3) == 6


def test_bunny_ears_5():
    assert bunny_ears(4) == 8


def test_bunny_ears_6():
    assert bunny_ears(5) == 10


def test_bunny_ears_7():
    assert bunny_ears(12) == 24


def test_bunny_ears_8():
    assert bunny_ears(50) == 100


def test_bunny_ears_9():
    assert bunny_ears(234) == 468
```
