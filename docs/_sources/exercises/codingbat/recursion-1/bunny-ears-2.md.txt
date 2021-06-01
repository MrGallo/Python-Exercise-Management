# bunny_ears_2





We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies (1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..) we'll say have 3 ears, because they each have a raised foot. Recursively return the number of "ears" in the bunny line 1, 2, ... n (without loops or multiplication).

```
bunny_ears_2(0) -> 0
bunny_ears_2(1) -> 2
bunny_ears_2(2) -> 5
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p107330) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def bunny_ears_2(bunnies: int) -> int:
    pass


result = bunny_ears_2(0)
print(result)
```

## Tests
```python
from main import bunny_ears_2


def test_bunny_ears_2_1():
    assert bunny_ears_2(0) == 0


def test_bunny_ears_2_2():
    assert bunny_ears_2(1) == 2


def test_bunny_ears_2_3():
    assert bunny_ears_2(2) == 5


def test_bunny_ears_2_4():
    assert bunny_ears_2(3) == 7


def test_bunny_ears_2_5():
    assert bunny_ears_2(4) == 10


def test_bunny_ears_2_6():
    assert bunny_ears_2(5) == 12


def test_bunny_ears_2_7():
    assert bunny_ears_2(6) == 15


def test_bunny_ears_2_8():
    assert bunny_ears_2(10) == 25
```
