# xyz_middle
**Topic:** 



Given a string, does "xyz" appear in the middle of the string? To define middle, we'll say that the number of chars to the left and right of the "xyz" must differ by at most one. This problem is harder than it looks.

```
xyz_middle("AAxyzBB") → true
xyz_middle("AxyzBB") → true
xyz_middle("AxyzBBB") → false
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p159772) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def xyz_middle(string: str) -> bool:
```

## Tests
```python
from main import xyz_middle


def test_xyz_middle_1():
    assert xyz_middle('AAxyzBB') == True


def test_xyz_middle_2():
    assert xyz_middle('AxyzBB') == True


def test_xyz_middle_3():
    assert xyz_middle('AxyzBBB') == False


def test_xyz_middle_4():
    assert xyz_middle('AxyzBBBB') == False


def test_xyz_middle_5():
    assert xyz_middle('AAAxyzB') == False


def test_xyz_middle_6():
    assert xyz_middle('AAAxyzBB') == True


def test_xyz_middle_7():
    assert xyz_middle('AAAAxyzBB') == False


def test_xyz_middle_8():
    assert xyz_middle('AAAAAxyzBBB') == False


def test_xyz_middle_9():
    assert xyz_middle('1x345xyz12x4') == True


def test_xyz_middle_10():
    assert xyz_middle('xyzAxyzBBB') == True


def test_xyz_middle_11():
    assert xyz_middle('xyzAxyzBxyz') == True


def test_xyz_middle_12():
    assert xyz_middle('xyzxyzAxyzBxyzxyz') == True


def test_xyz_middle_13():
    assert xyz_middle('xyzxyzxyzBxyzxyz') == True


def test_xyz_middle_14():
    assert xyz_middle('xyzxyzAxyzxyzxyz') == True


def test_xyz_middle_15():
    assert xyz_middle('xyzxyzAxyzxyzxy') == False


def test_xyz_middle_16():
    assert xyz_middle('AxyzxyzBB') == False


def test_xyz_middle_17():
    assert xyz_middle('') == False


def test_xyz_middle_18():
    assert xyz_middle('x') == False


def test_xyz_middle_19():
    assert xyz_middle('xy') == False


def test_xyz_middle_20():
    assert xyz_middle('xyz') == True


def test_xyz_middle_21():
    assert xyz_middle('xyzz') == True
```
