# del_del





Given a string, if the string "del" appears starting at index 1, return a string where that "del" has been deleted. Otherwise, return the string unchanged.

```
del_del("adelbc") → "abc"
del_del("adelHello") → "aHello"
del_del("adedbc") → "adedbc"
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p100905) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def del_del(string: str) -> str:
    pass


result = del_del('adelbc')
print(result)
```

## Tests
```python
from main import del_del


def test_del_del_1():
    assert del_del('adelbc') == 'abc'


def test_del_del_2():
    assert del_del('adelHello') == 'aHello'


def test_del_del_3():
    assert del_del('adedbc') == 'adedbc'


def test_del_del_4():
    assert del_del('abcdel') == 'abcdel'


def test_del_del_5():
    assert del_del('add') == 'add'


def test_del_del_6():
    assert del_del('ad') == 'ad'


def test_del_del_7():
    assert del_del('a') == 'a'


def test_del_del_8():
    assert del_del('') == ''


def test_del_del_9():
    assert del_del('del') == 'del'


def test_del_del_10():
    assert del_del('adel') == 'a'


def test_del_del_11():
    assert del_del('aadelbb') == 'aadelbb'
```
