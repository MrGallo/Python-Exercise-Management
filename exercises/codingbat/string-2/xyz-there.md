# xyz_there





Return true if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

```
xyz_there("abcxyz") → true
xyz_there("abc.xyz") → false
xyz_there("xyz.abc") → true
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p136594) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def xyz_there(string: str) -> bool:
    pass


result = xyz_there('abcxyz')
print(result)
```

## Tests
```python
from main import xyz_there


def test_xyz_there_1():
    assert xyz_there('abcxyz') == True


def test_xyz_there_2():
    assert xyz_there('abc.xyz') == False


def test_xyz_there_3():
    assert xyz_there('xyz.abc') == True


def test_xyz_there_4():
    assert xyz_there('abcxy') == False


def test_xyz_there_5():
    assert xyz_there('xyz') == True


def test_xyz_there_6():
    assert xyz_there('xy') == False


def test_xyz_there_7():
    assert xyz_there('x') == False


def test_xyz_there_8():
    assert xyz_there('') == False


def test_xyz_there_9():
    assert xyz_there('abc.xyzxyz') == True


def test_xyz_there_10():
    assert xyz_there('abc.xxyz') == True


def test_xyz_there_11():
    assert xyz_there('.xyz') == False


def test_xyz_there_12():
    assert xyz_there('12.xyz') == False


def test_xyz_there_13():
    assert xyz_there('12xyz') == True


def test_xyz_there_14():
    assert xyz_there('1.xyz.xyz2.xyz') == False
```
