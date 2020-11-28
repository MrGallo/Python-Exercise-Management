# count_code





Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

```
count_code("aaacodebbb") -> 1
count_code("codexxcode") -> 2
count_code("cozexxcope") -> 2
```

This exercise was taken from [codingbat.com](https://codingbat.com/prob/p123614) and has been adapted for the Python language. There are many great programming exercises there, but the majority are created for Java.

## Starter Code
```python
def count_code(string: str) -> int:
    pass


result = count_code('aaacodebbb')
print(result)
```

## Tests
```python
from main import count_code


def test_count_code_1():
    assert count_code('aaacodebbb') == 1


def test_count_code_2():
    assert count_code('codexxcode') == 2


def test_count_code_3():
    assert count_code('cozexxcope') == 2


def test_count_code_4():
    assert count_code('cozfxxcope') == 1


def test_count_code_5():
    assert count_code('xxcozeyycop') == 1


def test_count_code_6():
    assert count_code('cozcop') == 0


def test_count_code_7():
    assert count_code('abcxyz') == 0


def test_count_code_8():
    assert count_code('code') == 1


def test_count_code_9():
    assert count_code('ode') == 0


def test_count_code_10():
    assert count_code('c') == 0


def test_count_code_11():
    assert count_code('') == 0


def test_count_code_12():
    assert count_code('AAcodeBBcoleCCccoreDD') == 3


def test_count_code_13():
    assert count_code('AAcodeBBcoleCCccorfDD') == 2


def test_count_code_14():
    assert count_code('coAcodeBcoleccoreDD') == 3
```
